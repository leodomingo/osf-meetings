import Ember from 'ember';

export default Ember.Component.extend({
    toast : Ember.inject.service(),
    url : "files",
    dropzoneOptions : {
        uploadMultiple : false,
        method : 'PUT'
    },
    resolve : null,
    actions : {
        preUpload(comp, drop, file) {
            return new Ember.RSVP.Promise(resolve => {
                this.set('resolve', resolve);
            });
        },
        success() {
        },
        error() {
        },
        buildUrl(){
            return this.get('url');
        }
    }
});
