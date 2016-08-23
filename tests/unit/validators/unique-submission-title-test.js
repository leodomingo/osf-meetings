import { moduleFor, test } from 'ember-qunit';

moduleFor('validator:unique-submission-title', 'Unit | Validator | unique-submission-title', {
  needs: ['validator:messages']
});

test('it works', function(assert) {
  var validator = this.subject();
  assert.ok(validator);
});
