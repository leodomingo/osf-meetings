import Ember from 'ember';
import config from 'ember-get-config';

export function getUploadsUrl() {
  return config.uploadsUrl;
}

export default Ember.Helper.helper(getUploadsUrl);
