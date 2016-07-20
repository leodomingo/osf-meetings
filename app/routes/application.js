import Ember from 'ember';

export default Ember.Route.extend({
	didTransition: function() 
	{
		console.log(this.controllerFor('application').get('currentRouteName'));
	},
	actions: 
	{
		currentRoute: function()
		{
			console.log(this.controllerFor('application').get('currentRouteName'));
		},
		logout: function() 
		{
 		this.transitionTo('logout');
		},
		login: function() 
		{
			this.transitionTo('login');
		},
		filter(params) {
          this.transitionTo('index', {queryParams: {q: params}});
        },
        search(params)
        {
          this.transitionTo('search', {queryParams: {q: params, p:1}});
        }
	}
});
