import Ember from 'ember';

export default Ember.Route.extend({
	queryParams: {
		q: {
			refreshModel: true 
		}
	},

	model: function(params)
	{	
		return this.store.query('conference', {search:params.q});
	}
});
