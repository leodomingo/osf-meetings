import Ember from 'ember';
import Dropzone from 'npm:dropzone';

export default Ember.Component.extend({
	didRender(){
		this._super(...arguments);
		var dz = Dropzone.forElement("div#myDropzone");
		this.sendAction('getDropzone', dz);
	},
	setHeaders(file, xhr) {
		xhr.withCredentials = true;
        var csrftoken = Ember.get(document.cookie.match(/csrftoken\=([^;]*)/), "1");
        xhr.setRequestHeader('X-CSRFToken', csrftoken);
	},
	actions: {
		onSuccessfulUpload(file, responseText){
			this.sendAction('setFileUrlFromResponse', responseText.file);
		}
	}
});
