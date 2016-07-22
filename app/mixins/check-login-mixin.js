import Ember from 'ember';
import config from '../config/environment';

export default Ember.Mixin.create({
    //Overwrite redirectRoute function to return the route the user should transition to after logging in
    beforeModel: function() {
        var self = this;
        Ember.$.ajax({
            url: config.currentUser,
            dataType: 'json',
            contentType: 'text/plain',
            xhrFields: {
                withCredentials: true
            }
        }).then(function(loggedIn) {
            if (loggedIn.data === 'false') {
                self.transitionTo('login');
            }
        });
    },
    actions: {
        logout: function() {
            this.transitionToRoute('logout');
        }
    }
});
