import Ember from 'ember';

export default Ember.Component.extend({
	renaming: false,
	submission: '',
	actions: {
		clickRename(submission) {
			this.set('submission', submission);
			this.set('renaming', true);
		},
		confirm() {
			var self = this;
			this.get('submission').save().then(function() {
				self.set('renaming',false);
			});
		},
		cancel() {
			this.get('submission').rollbackAttributes();
		 	this.set('renaming', false);

		}
	}
});
