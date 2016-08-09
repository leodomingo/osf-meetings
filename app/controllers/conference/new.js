import Ember from 'ember';

export default Ember.Controller.extend({
	dropzone: null,
	actions: {
		setDropzone: function(dz){
			this.set('dropzone', dz);
			console.log(this.get('dropzone'));
		}
	}
});
