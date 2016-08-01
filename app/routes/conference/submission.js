import Ember from 'ember';
import CheckLoginMixin from 'osf-meetings/mixins/check-login-mixin';


export default Ember.Route.extend(CheckLoginMixin, {
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
