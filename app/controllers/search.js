import Ember from 'ember';

export default Ember.Controller.extend({
	query: null,
	results: null,
	store: Ember.inject.service('store'),
	queryParams: ['q', 'p'],
	page: 1,
	actions: 
	{
      search() {
        let query = this.get("searchQuery");
        this.set('query', query);
		this.transitionToRoute('search', {queryParams: {q: query, p: this.page }});
		},
	  forward(){
		this.set('page',this.page+1);
		this.send('search');
		var model = this.get('model');
		},
	  back(){
		this.set('page',this.page-1);
		this.send('search');
		},
		toPage(pageNum){
			let query = this.get("searchQuery");
			this.transitionToRoute('search', {queryParams: {q: query, p: pageNum }});
		}
    }
});
