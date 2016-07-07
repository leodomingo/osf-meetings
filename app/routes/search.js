import Ember from 'ember';

export default Ember.Route.extend({
	page: 1,
	queryParams: {
		q: {refreshModel: true},
		p: {refreshModel: true}
	},

	model: function(params)
	{	

		let foundConferences =  this.store.query('conference', {search:params.q, page: params.p});
		console.log(foundConferences.length);
		return foundConferences;
	}
});
