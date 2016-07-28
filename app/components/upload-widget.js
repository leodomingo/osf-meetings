import Ember from 'ember';

export default Ember.Component.extend({
    store : Ember.inject.service(),
    toast : Ember.inject.service(),
    url : 'http://localhost:8000/files/?submissionId=',
    file : null,
    dropzoneOptions : {
        uploadMultiple : false,
        method : 'POST',
        xhrFields : { withCredentials : true },
        crossDomain : true
    },
    resolve : null,
    dropZone : null,
    actions : {
        preUpload(comp, drop, file) {
            //console.log(drop);
            this.set('dropZone', drop);
            return new Ember.RSVP.Promise(resolve => {
                this.set('resolve', resolve);
            });
        },
        success() {
        },
        error() {
            console.log('ERROR');
        },
        buildUrl(){
            return this.get('url');
        }
    }
});
