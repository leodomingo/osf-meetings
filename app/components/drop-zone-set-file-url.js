import Ember from 'ember';

export default Ember.Component.extend({
	setHeaders(file, xhr) {
		xhr.withCredentials = true;
        var csrftoken = Ember.get(document.cookie.match(/csrftoken\=([^;]*)/), "1");
        xhr.setRequestHeader('X-CSRFToken', csrftoken);
	},
	actions: {
		onSuccessfulUpload(file, responseText){
			this.sendAction('setUploadFromResponse', responseText);
		},
		onRemovedFile(file){
			this.sendAction('setFileUrlFromResponse', '');
		}
	}
});
