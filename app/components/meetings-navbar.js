import Ember from 'ember';
import config from 'ember-get-config';
import {
    getAuthUrl
} from 'ember-osf/utils/auth';


export default Ember.Component.extend({
    authenticated: false,
    router: Ember.inject.service('router'),
    session: Ember.inject.service(),
    currentUser: null,
    gravatarUrl: null,
    fullName: null,
    user: null,
    showSearch: false,
    init: function(){
        this._super(...arguments);
        var self = this;
        Ember.$.ajax({
            url: "http://localhost:8000/current/",
            dataType: 'json',
            contentType: 'text/plain',
            xhrFields: {
                withCredentials: true,
            }
        }).then(function(loggedIn) {
            if (loggedIn.data !=='false')
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
