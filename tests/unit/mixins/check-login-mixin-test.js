import Ember from 'ember';
import CheckLoginMixinMixin from 'osf-meetings/mixins/check-login-mixin';
import { module, test } from 'qunit';

module('Unit | Mixin | check login mixin');

// Replace this with your real tests.
test('it works', function(assert) {
  let CheckLoginMixinObject = Ember.Object.extend(CheckLoginMixinMixin);
  let subject = CheckLoginMixinObject.create();
  assert.ok(subject);
});
