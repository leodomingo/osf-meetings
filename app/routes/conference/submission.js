import Ember from 'ember';

export default Ember.Route.extend({
    model(params) {
        var conf = this.store.peekRecord('conference', params.conference_id);
        return this.store.createRecord('submission', {
            conference : conf
        });
    },

    actions : {
        saveSubmission(newSubmission) {
            var router = this;
            newSubmission.save().then(function(newRecord){
                var newRecord_Conf = newRecord.get('conference');
                router.transitionTo('conference.index', newRecord_Conf.get('id'));
            });
        }
    }
});
