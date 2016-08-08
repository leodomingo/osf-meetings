import { moduleForComponent, test } from 'ember-qunit';
import hbs from 'htmlbars-inline-precompile';
import startMirage from '../../helpers/start-mirage';


moduleForComponent('meeting-masonry', 'Integration | Component | meeting masonry', {
  integration: true,
  setup() {
    startMirage(this.container);
  }
});

test('it renders', function(assert) {
  // Set any properties with this.set('myProperty', 'value');
  // Handle any actions with this.on('myAction', function(val) { ... });

  const model = server.create('conference');
  this.set('model', model);
  let testDescription = this.get('model').description.substring(0,200) + "...";
  this.render(hbs`{{meeting-masonry model=model}}`);


  assert.equal(this.$('.tile-title').text().trim(), model.title);
  assert.equal(this.$('.tile-description').text().trim(), testDescription);


});

