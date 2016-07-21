import Ember from 'ember';
import EmberUploader from 'ember-uploader';

export default EmberUploader.FileField.extend({
    url : null,

    filesDidChange : function(files) {
        const uploader = EmberUploader.Uploader.create({
            url : this.get('url'),
            method : 'PUT'
        });
    }
});
