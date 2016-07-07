import Ember from 'ember';

export default Ember.Controller.extend({
	queryParams: ['q', 'p'],
	category: null,
	page: 1,
	actions: 
	{
      search() {
        let query = this.get("searchQuery");
		this.transitionToRoute('search', {queryParams: {q: query, p: this.page }});
		},
	  moreResults(){
		this.set('page',this.page+1);
		this.send('search');
		}
    }
});
