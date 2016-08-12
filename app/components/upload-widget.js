import Ember from 'ember';

export default Ember.Component.extend({
    toast : Ember.inject.service(),
    file : null,
    url: null,
    dropzoneOptions : {
        uploadMultiple : false,
        crossDomain : true
    },
    resolve : null,
    dropZone : null,
    actions : {
        preUpload() {
            this.set('dropZone', arguments[1]);
            return new Ember.RSVP.Promise(resolve => {
                this.set('resolve', resolve);
            });
        },
        success(_this, dropZone, file, successData) {
            this.sendAction('success', dropZone, file, successData);
        },
        error() {
            //do toast here
            console.log('ERROR');
        },
        buildUrl(){
            return this.get('url');
        }
    }
});
