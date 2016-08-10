import Ember from 'ember';

export default Ember.Component.extend({
    store: Ember.inject.service('store'),
    tagName: 'tr',
    isRenaming: false,
    displayModal: false,
    actions: {
        clickRename() {
            this.set('isRenaming', true);
        },
        clickDelete() {
            this.set('displayModal', true);
        },
        confirmRename(submission) {
            this.set('isRenaming', false);
            submission.save();
        },
        confirmDelete(submission) {
            this.set('displayModal', false);
            submission.destroyRecord();
        },
        cancelRename(submission) {
            this.set('isRenaming', false);
            submission.rollbackAttributes();
        },
        cancelDelete() {
            this.set('displayModal', false);
        },
        download(uri) {
            debugger;
            var link = document.createElement("a");
            link.download = '';
            link.href = uri;
            link.click();
        }
    }
});
