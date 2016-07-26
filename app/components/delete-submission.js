import Ember from 'ember';

export default Ember.Component.extend({
	submission: '',
	displayModal: false,
	actions: {
		clickDelete (submission) {
			this.set('submission', submission);
			this.set('displayModal', true);
		},
		deleteSubmission() {
			this.get('submission').destroyRecord();
		},
		cancel() {
			this.set('displayModal', false);
		}
	}
});
