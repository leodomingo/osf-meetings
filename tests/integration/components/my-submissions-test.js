import { moduleForComponent, test } from 'ember-qunit';
import hbs from 'htmlbars-inline-precompile';
import startMirage from '../../helpers/start-mirage';
import moment from 'moment';


moduleForComponent('my-submissions', 'Integration | Component | my submissions', {
  integration: true,
  setup() {
    startMirage(this.container);
  }
});

function dateDisplay(val) {
    var date = new Date(val);
    return moment(date).format("MM-DD-YYYY");
}

test('it renders', function(assert) {
  // Set any properties with this.set('myProperty', 'value');
  // Handle any actions with this.on('myAction', function(val) { ... });

  const model = server.create('submission');
  this.set('model', model);
  this.render(hbs`{{my-submissions submission=model}}`);
  assert.equal(this.$(".tableCategory").text().trim(), model.category);
  assert.equal(this.$('.tableTitle').text().trim(), model.title);
  assert.equal(this.$('.tableDate').text().trim(), dateDisplay(model.dateCreated));
  assert.equal(this.$('.tableDownloadCount').text().trim(), model.downloadCount);



});
