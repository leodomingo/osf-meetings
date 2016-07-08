import Ember from 'ember';

export default Ember.Route.extend({
	page: 1,
	queryParams: {
		q: {refreshModel: true},
		p: {refreshModel: true}
	},

	model: function(params)
	{	
		this.store.unloadAll();
		let foundConferences =  this.store.query('conference', {search:params.q, page: params.p});
		return foundConferences;
	}
});
