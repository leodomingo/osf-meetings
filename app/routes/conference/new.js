import Ember from 'ember';
import CheckLoginMixin from 'osf-meetings/mixins/check-login-mixin';
import config from '../../config/environment';


export default Ember.Route.extend(CheckLoginMixin, {
    model() {
        return Ember.RSVP.hash({
            meta : Ember.$.ajax({
                url : config.meetingsUrl + "conferences/",
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
        saveNode(newConf) {
            var router = this;
            newConf.save().then(function(params) {
                router.transitionTo('conference.index', params.id);
            });
        }
    }
});
