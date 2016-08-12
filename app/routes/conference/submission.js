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
                    drop.on('processing', function(file) {
                        var that = this;
                        this.options.url = config.providers.osf.uploadsUrl + 
                            newRecord.get('nodeId') +
                            '/providers/osfstorage/?kind=file&name=' + 
                            file.name;
                        var userId = newRecord.get('contributor').then((authUser) =>{
                            var authHeader = 'Bearer ' + authUser.get('token');
                            that.options.headers = {
                                'Authorization' : authHeader
                            }
                        });
                        this.options.method = 'PUT';
                    });     
                    resolve();                    
                });
        },

        success(dropZone, file, successData) {
            var nodeId = successData['data']['attributes']['resource']; //osf node's id
            var submissions = this.get('store').peekAll('submission');
            var relatedSubmission = submissions.findBy('nodeId', nodeId);

            var newFile = this.get('store').createRecord('metafile', {
                submission : relatedSubmission,
                osfId : successData['data']['id'],
                osfUrl : successData['data']['links']['download'],
                fileName : successData['data']['attributes']['name']
            });

            newFile.save().then((metafile) => {
                //do toast here
                var submission = metafile.get('submission');
                var conf = submission.get('conference');
                this.transitionTo('conference.index', conf.get('id'));
            });
        }
    }
});
