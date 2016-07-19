import Ember from 'ember';

export default Ember.Route.extend({
	actions: 
	{
		logout: function() 
		{
			this.transitionToRoute('logout');
		},
		login: function() 
		{
			console.log("fired application action");
			this.transitionTo('login');
		}
	}
});
