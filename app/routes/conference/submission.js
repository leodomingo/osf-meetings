import Ember from 'ember';
import CheckLoginMixin from 'osf-meetings/mixins/check-login-mixin';


export default Ember.Route.extend(CheckLoginMixin, {
    model() {
        return this.store.createRecord('submission');
    },

    actions : {
        saveSubmission(newSubmission) {
            var conference = this.modelFor('conference.index');
            this.store.adapterFor('submission').set('namespace', `conferences/${conference.id}`);
            newSubmission.set('conference', conference);
            newSubmission.save().then(function(newRecord){
                console.log(newRecord);
            });
        }
    }
});
