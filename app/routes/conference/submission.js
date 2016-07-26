import Ember from 'ember';
import CheckLoginMixin from 'osf-meetings/mixins/check-login-mixin';


export default Ember.Route.extend(CheckLoginMixin, {
    model(params) {
        this.store.adapterFor('submission').set('namespace',
            `conferences/${params.conference_id}`);
        var conf = this.store.peekRecord('conference', params.conference_id);
        return this.store.createRecord('submission', {
            conference : conf
        });
    },

    actions : {
        saveSubmission(newSubmission, resolve) {
            if(resolve) {
                newSubmission.save().then((newRecord) => {
                    resolve.then((file) => {
                        console.log(file);
                    });
                });
            } else {
                console.log("resolve error");
            }
        }
    }
});
