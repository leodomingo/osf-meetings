import Ember from 'ember';
import config from '../config/environment';


// The check-login-mixin should be included on routes for which only logged-in users can see.
// The mixin checks if the user is logged in and redirects them to the login workflow if they
// are not logged in. It also stores the current URL in a cookie and after logging in, checks
// the cookie and gets back to the original page.


export default Ember.Mixin.create({
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
                if (window.location.href !== config.meetingsHomeUrl) {
                    document.cookie = "redirectURL=" + window.location.href;
                } else {
                    document.cookie = "redirectURL=" + config.meetingsHomeUrl + "conference/new/";
                }
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
