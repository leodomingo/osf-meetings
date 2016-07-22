import Ember from 'ember';
import config from '../config/environment';

export default Ember.Component.extend({
    routing: Ember.inject.service('-routing'),
    host: config.osfUrl,
    authenticated: false,
    frontPage: null,
    user: null,
    init: function(){   
        this._super(...arguments);
        var self = this;
        var currentRoute = this.get('routing').get('currentRouteName');
        if (currentRoute === 'index'){
            self.set('frontPage', true);
        }
        else {
            self.set('frontPage', false);
        }
        Ember.$.ajax({
            url: config.currentUser,
            dataType: 'json',
            contentType: 'text/plain',
            xhrFields: {
                withCredentials: true,
            }
        }).then(function(loggedIn) {
            if (!(loggedIn.data.errors) && (loggedIn.data !== 'false'))
            {
                self.set('authenticated', true);
                self.set('user', loggedIn.data.data);
            }
            else 
            {
                self.set('authenticated', false);
                self.set('user', null);
            }
        });
    },
	actions: 
	{
		filter: function() 
		{
			this.sendAction('filter', this.get("searchQuery"));
		},
		search: function() 
		{
			this.sendAction('search', this.get("searchQuery"));
		},
        logout: function() 
        {   
            this.sendAction('logout');
        },
        login: function() 
        {
            this.sendAction('login');
        }
	}
});
