import Ember from 'ember';
import config from '../../config/environment';

// Validations are currently disabled for developing. They will likely need to be completely 
// re-implemented. Currently they are set up using the ember-validations library which only
// works with model variables. However, we have since changed our implementation so that the 
// model does not exist while the route is loaded, and the model is only generated after the form
// has been filled out. Because of this, model variables no longer exist on the page. So unless
// there is a reason to go back to creating the model when the page is loaded, an alternate 
// validations library will need to be used.

export default Ember.Route.extend({

    model() {
        return Ember.RSVP.hash({
                meta : Ember.$.ajax({
                url : config.providers.osfMeetings.apiUrl + "conferences/",
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
            newConf.save().then(function(params) {
                router.transitionTo('conference.index', params.id);
            });
        },
        count(){
            //console.log('Got one');
            let maxLength = 500;
            let remainder = maxLength -Ember.$('#description').val().length;
            if ((remainder < 0) || (remainder > 470)){
                Ember.$('#remaining').css({"color" : "red"});
            }
            else {
                Ember.$('#remaining').css({'color' : 'green'});
            }
            Ember.$('#remaining').text(remainder);
        }
    }
});
