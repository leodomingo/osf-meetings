import Ember from 'ember';

export default Ember.Controller.extend({
	queryParams: 'q',
	category: null,
	actions: 
	{
      search() 
      {
        let query = this.get("searchQuery");
		this.transitionToRoute('search', {queryParams: {q: query}});
		}
    }
});
