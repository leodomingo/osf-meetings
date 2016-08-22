import Ember from 'ember';
import config from 'ember-get-config';

export function linkToOsf(params) {

  return config.providers.osf.host + params;
}

export default Ember.Helper.helper(linkToOsf);
