import Ember from 'ember';

export default Ember.Component.extend({
    store : Ember.inject.service(),
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
            console.log('\n\n preUpload \n\n');
            console.log(...arguments);
            this.set('dropZone', arguments[1]);
            return new Ember.RSVP.Promise(resolve => {
                this.set('resolve', resolve);
            });
        },
        success() {

            //might need to move to router for transition
            //need router-action module if so
            var successData = arguments[3];
            var nodeId = successData['data']['attributes']['resource'];
            var submissions = this.get('store').peekAll('submission');
            var relatedSubmission = submissions.findBy('nodeId', nodeId);

            var newFile = this.get('store').createRecord('file', {
                submission : relatedSubmission,
                owner : relatedSubmission.get('contributor'),
                osfId : successData['data']['id'],
                osfUrl : successData['data']['links']['download'],
                fileName : successData['data']['attributes']['name']
            });

            newFile.save();

        },
        error() {
            console.log('ERROR');
            console.log(...arguments);
            //debugger;
        },
        buildUrl(){
            return this.get('url');
        }
    }
});
