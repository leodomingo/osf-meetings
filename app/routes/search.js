import Ember from 'ember';

export default Ember.Route.extend({
	pages: null,
	results: null,
	queryParams: {
		q: {refreshModel: true},
		p: {refreshModel: true}
	},
	beforeModel: function(params)
	{
			this.set('results', this.store.query('conference', {search:params.q, page: params.p}));
	},
	model: function(params)
	{	
		//console.log(this.get('pages'));
		let foundConferences = this.store.query('conference', {search:params.q, page: params.p}).then((result) => {
				this.set('results', true);
  				let meta = result.get('meta');
  				this.set('pages', meta.pagination.pages);
  				if(meta.pagination.count == 0)
  				{
  					this.set('results', false);
  				}
  				return result;
		});
		//console.log(foundConferences.get('length'));
		return foundConferences;
	},
	setupController: function(controller, model)
	{
		this._super(controller, model);
		this.controllerFor('search').set('results', this.get('results'));
	}
});
