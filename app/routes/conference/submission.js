import Ember from 'ember';

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
