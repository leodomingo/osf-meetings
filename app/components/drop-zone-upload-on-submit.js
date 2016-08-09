import Ember from 'ember';

export default Ember.Component.extend({
	didInsertElement() {
	  this._super(...arguments);
	  var dz = Ember.$('#myDropzone');
	  this.sendAction('setDropzone', dz);
	}
});
