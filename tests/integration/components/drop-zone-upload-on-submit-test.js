import { moduleForComponent, test } from 'ember-qunit';
import hbs from 'htmlbars-inline-precompile';

moduleForComponent('drop-zone-upload-on-submit', 'Integration | Component | drop zone upload on submit', {
  integration: true
});

test('it renders', function(assert) {
  // Set any properties with this.set('myProperty', 'value');
  // Handle any actions with this.on('myAction', function(val) { ... });

  this.render(hbs`{{drop-zone-upload-on-submit}}`);

  assert.equal(this.$().text().trim(), '');

  // Template block usage:
  this.render(hbs`
    {{#drop-zone-upload-on-submit}}
      template block text
    {{/drop-zone-upload-on-submit}}
  `);

  assert.equal(this.$().text().trim(), 'template block text');
});
