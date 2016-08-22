import Ember from 'ember';
import config from 'ember-get-config';

// Validations are currently disabled for developing. They will likely need to be completely 
// re-implemented. Currently they are set up using the ember-validations library which only
// works with model variables. However, we have since changed our implementation so that the 
// model does not exist while the route is loaded, and the model is only generated after the form
// has been filled out. Because of this, model variables no longer exist on the page. So unless
// there is a reason to go back to creating the model when the page is loaded, an alternate 
// validations library will need to be used.

export default Ember.Route.extend({
    model(params) {
        var conf = this.store.peekRecord('conference', params.conference_id);
        return this.store.createRecord('submission', {
            conference : conf
        });
    },

    actions : {
        saveSubmission(newSubmission, drop, resolve) {
                newSubmission.save().then((newRecord) => {
                    drop.options.url = config.providers.osf.uploadsUrl + 
                        newRecord.get('nodeId') +
                        '/providers/osfstorage/?kind=file&name=' + 
                        drop.getQueuedFiles()[0].name;
                    var userId = newRecord.get('contributor').then((authUser) =>{
                        var authHeader = 'Bearer ' + authUser.get('token');
                        drop.options.headers = {
                            'Authorization' : authHeader
                        }
                        resolve();
                    });      
                });                     
        },
        preUpload(drop){
            drop.options.method = 'PUT';
        },
        success(dropZone, file, successData) {
            var router = this;
            var nodeId = successData['data']['attributes']['resource']; //osf node's id
            var submissions = this.get('store').peekAll('submission');
            var relatedSubmission = submissions.findBy('nodeId', nodeId);

            var newFile = this.get('store').createRecord('metafile', {
                submission : relatedSubmission,
                osfId : successData['data']['id'],
                osfUrl : successData['data']['links']['download'],
                fileName : successData['data']['attributes']['name']
            });

            newFile.save().then((file) => {
                //do toast here
                var submission = file.get('submission');
                var conf = submission.get('conference');
                router.transitionTo('conference.index', conf.get('id'));
            });
        }
    }
});
