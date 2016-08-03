import Ember from 'ember';

export default Ember.Route.extend({
    model(params) {
        var conf = this.store.peekRecord('conference', params.conference_id);
        return this.store.createRecord('submission', {
            conference : conf
        });
    },

    //Need to fix the routing after submission
    actions : {
        saveSubmission(newSubmission, drop, resolve) {
//            var router = this;

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

//                    drop.on('sending', function(file, xhr, formData) {
//                        var newFile = router.store.createRecord('file', {
//                            submission : newRecord,
//                            owner : newRecord.get('contributor')
//                        });
//
//                    });
//                    var newRecord_Conf = newRecord.get('conference');
//                    router.transitionTo('conference.index', newRecord_Conf.get('id'));
                });

            } else {
                console.log("Upload Error");
            }
        }
    }
});
