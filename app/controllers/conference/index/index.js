// This file isn't currently used. We are moving away from controllers and towards using
// components for controller based actions. Using components will be much more sustainable
// for furute versions of ember.


import Ember from 'ember';
import EmberValidations from 'ember-validations';

export default Ember.Controller.extend(EmberValidations, {

	editing: false,
	navModal: false,
	displayErrors: false,
	info: false,

 	hasState: Ember.computed.match('model.state', /.+/),

	actions: {
		selectCountry(country) {
      		this.set('model.country', country);
    	},
		editConference() {
			this.set('editing',true);
		},	
		cancelEdits() {
			this.set('editing',false);
			this.set('displayErrors',false);
			this.store.findRecord('conference',this.get('model.id')).then(function(conference) {
				conference.rollbackAttributes();
			});
		},
		saveEdits(conferenceID) {
	      	if (this.get('isValid')) {
				var conference = this.store.peekRecord('conference', conferenceID);
				conference.save();
				this.set('editing',false);
				this.set('displayErrors',false);
			} else {
				this.set('displayErrors',true);
			}
		}
	}
});
