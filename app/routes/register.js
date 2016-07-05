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
    deactivate: function() {
        var controller = this.get('controller');
        controller.send('killConference');
        controller.set('kill',true);
        controller.set('displayErrors',false);
    },
    actions: {
        back() {
            this.transitionTo('index').then(function(newRoute) {
                newRoute.controller.set('visited', true);
            });
        },
        saveNode(newConf) {
            var router = this;
//            var subend = newConf.get('submissionend');
//            subend = subend.toISOString();
//            var substart = newConf.get('submissionstart');
//            substart = substart.toISOString();
//            var end = newConf.get('end');
//            end = end.toISOString();
//            var start = newConf.get('start');
//            start = start.toISOString();
//            newConf.set('submissionend', subend);
//            newConf.set('submissionstart', substart);
//            newConf.set('end', end);
//            newConf.set('start', start);
            newConf.save().then(function(params) {
                router.transitionTo('conference.index', params.id); //.then(function(newRoute) {
                    //newRoute.controller.set('visited', true);
                //});
            });
        }
    }
});
