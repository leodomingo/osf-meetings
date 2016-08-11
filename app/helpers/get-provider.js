import Ember from 'ember';
import config from 'ember-get-config';

export function getProvider(params/*, hash*/) {
	var providerName = params[0];
	return config.providers[providerName];
}

export default Ember.Helper.helper(getProvider);
