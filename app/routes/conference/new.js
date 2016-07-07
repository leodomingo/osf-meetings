import Ember from 'ember';

export default Ember.Route.extend({
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
        saveNode(newConf) {
            var router = this;
            newConf.save().then(function(params) {
                router.transitionTo('conference.index', params.id);
            });
        }
    }
});
