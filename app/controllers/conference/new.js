import Ember from 'ember';

export default Ember.Controller.extend({
	dropzone: null,
	actions: {
		getDropzone: function(dz){
			this.set('dropzone', dz);
		}
	}
});
