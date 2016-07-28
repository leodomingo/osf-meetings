import Ember from 'ember';
import CheckLoginMixin from 'osf-meetings/mixins/check-login-mixin';


export default Ember.Route.extend(CheckLoginMixin, {
    model(params) {
        this.store.adapterFor('submission').set('namespace',
            `conferences/${params.conference_id}`);
        var conf = this.store.peekRecord('conference', params.conference_id);
        return this.store.createRecord('submission', {
            conference : conf,
        });
    },

    url : null,

    actions : {
        saveSubmission(newSubmission, drop, resolve) {
            var response = Ember.$.ajax({
                url: 'https://staging-api.osf.io/v2/nodes/',
                type: 'POST',
                data: newSubmission,
                headers : {
                    'Authorization' : 'Bearer ' + token
                }
            });

            if(resolve) {
                newSubmission.save().then((newRecord) => {
                    resolve();
                    drop.on('processing', function(file) {
                        this.options.url = this.options.url() + newRecord.id;
                    });
//                    let newFile = route.store.createRecord('file', {
//                        submission : newRecord
//                    });
                });
            } else {
                console.log("resolve error");
            }
        }
    }
});
