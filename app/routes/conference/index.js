import Ember from 'ember';

export default Ember.Route.extend({
    model(params) {
        this.store.adapterFor('submission').set('namespace', `conferences/${params.conference_id}`);
        return Ember.RSVP.hash({
            conf : this.store.find('conference', params.conference_id),
            submissions : this.store.findAll('submission')
        });
    },
    actions: {
    	download(uri) {
		  var link = document.createElement("a");
		  link.download = '';
		  link.href = uri;
		  link.click();
		},
		deleteSubmission(conferenceId, submissionId) {
			Ember.$.ajax({
				url : ("http://localhost:8000/conferences/" + conferenceId + "/submissions/" + submissionId + "/"),
                type : "DELETE",
			}).then(function () {
				location.reload();
			});
		}
    }
});
