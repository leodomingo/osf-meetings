import Model from 'ember-data/model';
import attr from 'ember-data/attr';
import { belongsTo } from 'ember-data/relationships';

export default Model.extend({
	date_created: attr('isodate', { defaultValue : (new Date()).toISOString() }),
	file: attr('string', { defaultValue : '' }),
	conference: belongsTo('conference', { async : true }),
});
