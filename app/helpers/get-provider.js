import Ember from 'ember';
import config from 'ember-get-config';

export function getProvider(provider_name) {
	return config.providers[provider_name];
}

export default Ember.Helper.helper(getProvider);
