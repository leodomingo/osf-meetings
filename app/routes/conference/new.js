import Ember from 'ember';
import config from '../../config/environment';

export default Ember.Route.extend({
    model() {
        return Ember.RSVP.hash({
            meta : Ember.$.ajax({
                url : config.meetingsUrl + "/conferences/",
                type : "OPTIONS",
                xhrFields : {
                    withCredentials : true
                },
                crossDomain : true
            }),
            newConf : this.store.createRecord('conference')
        });
    },

    actions: {
        back() {
            this.transitionTo('index').then(function(newRoute) {
                newRoute.controller.set('visited', true);
            });
        },
        saveConference(newConf) {
            var router = this;
            console.log(newConf.logo.id);
            newConf.save().then(function(params) {
                router.transitionTo('conference.index', params.id);
            });
        },
        setUpload(response){
            var newConf = this.currentModel.newConf;
            var upload = this.store.findRecord('upload', response.id).then(function(record){
                newConf.set('logo', record);
            });
        }
    }
});
