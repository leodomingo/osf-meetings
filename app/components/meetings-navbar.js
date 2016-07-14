import Ember from 'ember';

export default Ember.Component.extend({
	actions: 
	{
		filter: function() 
		{
			this.sendAction('filter', this.get("searchQuery"));
		},
		search: function() 
		{
			this.sendAction('search', this.get("searchQuery"));
		}
	}
});
