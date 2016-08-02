import Ember from 'ember';

export default Ember.Route.extend({
    model(params) {
        var conf = this.store.peekRecord('conference', params.conference_id);
        return this.store.createRecord('submission', {
            conference : conf,
        });
    },

    url : null,

    actions : {
//        saveSubmission(newSubmission) {
//            var router = this;
//            newSubmission.save().then(function(newRecord){
//                var newRecord_Conf = newRecord.get('conference');
//                router.transitionTo('conference.index', newRecord_Conf.get('id'));
//            });
//        },
//
        saveSubmission(newSubmission, drop, resolve) {
            if(resolve) {
                newSubmission.save().then((newRecord) => {
                    resolve();
                    drop.on('processing', function(file) {
                        //this.options.url = this.options.url() + newRecord.get('nodeId');
                        this.options.url = this.options.url() + newRecord.id;
                    });
                });
            } else {
                console.log("resolve error");
            }
        }
    }
});
