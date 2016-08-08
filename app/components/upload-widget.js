import Ember from 'ember';

export default Ember.Component.extend({
    store : Ember.inject.service('store'),
    toast : Ember.inject.service(),
    url : 'https://staging-files.osf.io/v1/resources/',
    file : null,
    dropzoneOptions : {
        uploadMultiple : false,
        method : 'PUT',
        xhrFields : { withCredentials : true },
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
        success() {
            var that = this;
            var successData = arguments[3];
            var nodeId = successData['data']['attributes']['resource']; //osf node's id
            var submissions = this.get('store').peekAll('submission');
            var relatedSubmission = submissions.findBy('nodeId', nodeId);

            var newFile = this.get('store').createRecord('metafile', {
                submission : relatedSubmission,
                osfId : successData['data']['id'],
                osfUrl : successData['data']['links']['download'],
                fileName : successData['data']['attributes']['name']
            });

            newFile.save().then((file) => {
                //do toast here
                that.sendAction('success', file);
            });
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
