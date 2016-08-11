import Ember from 'ember';
import config from 'ember-get-config';

export function getProvider(params/*, hash*/) {
	var provider_name = params[0];
	return config.providers[provider_name];
}

export default Ember.Helper.helper(getProvider);
