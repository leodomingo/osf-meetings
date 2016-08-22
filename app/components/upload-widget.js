import Ember from 'ember';
import config from 'ember-get-config';

export default Ember.Component.extend({
    toast : Ember.inject.service(),
    file : null,
    url: null,
    dropzoneOptions : {
        uploadMultiple : false,
        xhrFields : { withCredentials : true },
        crossDomain : true
    },
    resolve : null,
    dropZone : null,
    actions : {
        preUpload() {
            var drop = arguments[1];
            this.set('dropZone', drop);
            this.sendAction('preUpload', drop);
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
