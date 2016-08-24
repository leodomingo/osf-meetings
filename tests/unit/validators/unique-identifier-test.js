import { moduleFor, test } from 'ember-qunit';

moduleFor('validator:unique-identifier', 'Unit | Validator | unique-identifier', {
  needs: ['validator:messages']
});

test('it works', function(assert) {
  var validator = this.subject();
  assert.ok(validator);
});
