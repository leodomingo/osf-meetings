import Ember from 'ember';

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
            if(resolve) {
                newSubmission.save().then((newRecord) => {
                    resolve();
                    drop.on('processing', function(file) {
                        this.options.url = this.options.url() + newRecord.get('nodeId') +
                            '/providers/osfstorage/?kind=file&name=' + file.name;
                        var authUser = newRecord.get('contributor');
                        this.options.headers = {
                            'Authorization' : 'Bearer ' + authUser.get('token')
                        };
                    });
                });

            } else {
                console.log("Upload Error");
            }
        },

        success(metafile) {
            var submission = metafile.get('submission');
            var conf = submission.get('conference');
            this.transitionTo('conference.index', conf.get('id'));
        }
    }
});
