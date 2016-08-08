import Model from 'ember-data/model';
import attr from 'ember-data/attr';
import { belongsTo } from 'ember-data/relationships';

export default Model.extend({
    conference : belongsTo('conference', { async : true }),
    title : attr('string'),
    description : attr('string'),
    canEdit: attr('boolean'),
    nodeId: attr('string'),
    category: attr('string', { defaultValue : 'project' }),
    metafile : belongsTo('metafile'),
    dateCreated: attr(),
    downloadLink: attr('string'),
    downloadCount: attr('string'),
    contributor : belongsTo('user')
});
