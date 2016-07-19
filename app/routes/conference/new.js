import Ember from 'ember';
import CheckLoginMixin from 'osf-meetings/mixins/check-login-mixin';


export default Ember.Route.extend(CheckLoginMixin, {
    model() {
        return Ember.RSVP.hash({
            meta : Ember.$.ajax({
                url : "http://localhost:8000/conferences/",
                type : "OPTIONS"
            }),
            newConf : this.store.createRecord('conference')
        });
    },
//    deactivate: function() {
//        var controller = this.get('controller');
//        controller.send('killConference');
//        controller.set('kill',true);
//        controller.set('displayErrors',false);
//    },
    actions: {
        back() {
            this.transitionTo('index').then(function(newRoute) {
                newRoute.controller.set('visited', true);
            });
        },
        saveConference(newConf) {
            var router = this;
            newConf.save().then(function(params) {
                router.transitionTo('conference.index', params.id);
            });
        }
    }
});
