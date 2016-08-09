import Ember from 'ember';

export default Ember.Component.extend({
	didRender(){
		this._super(...arguments);
		var dz = Ember.$('#myDropzone');
		this.sendAction('getDropzone', dz);
	}
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
