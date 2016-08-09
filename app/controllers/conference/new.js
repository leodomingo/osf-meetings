import Ember from 'ember';

export default Ember.Controller.extend({
	dropzone: null,
	getDropzone: function(dz){
		this.set('dropzone', dz);
	}
});
