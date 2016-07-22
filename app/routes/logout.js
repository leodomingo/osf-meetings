import Ember from 'ember';

export default Ember.Route.extend({
	activate: function() {
        window.location = "http://localhost:8000/accounts/logout/";
    }
});
