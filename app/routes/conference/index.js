import Ember from 'ember';

export default Ember.Route.extend({
	model() {
		return this.store.findAll('node')
	},
	action: {
		saveNodeSubmission(newNode){
	    	var router = this;
	    	newNode.save().then(function(){
	    		router.transitionTo('conference');
	    	});
	    }
	}
});