import Ember from 'ember';
import config from '../config/environment';

export default Ember.Route.extend({
    activate: function() {
        window.location = config.meetingsUrl + "/accounts/login/";
    }
});

