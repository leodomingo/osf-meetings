import attr from 'ember-data/attr';
//import Collection from './collection';
import Model from 'ember-data/model';
import { hasMany, belongsTo } from 'ember-data/relationships';

export default Model.extend({
    title: attr('string'),
    city: attr('string'),
    state: attr('string'),
    country: attr('string'),
    eventStart: attr('isodate', { defaultValue : (new Date()).toISOString() }),
    eventEnd: attr('isodate', { defaultValue : (new Date()).toISOString() }),
    submissionStart: attr('isodate', { defaultValue : (new Date()).toISOString() }),
    submissionEnd: attr('isodate', { defaultValue : (new Date()).toISOString() }),
    description: attr('string'),
    site: attr('string', { defaultValue : '' }),
    logo: belongsTo('upload', { async : true }),
    submissions : hasMany('submission', { async : true }),
    canEdit: attr('boolean', { defaultValue : ''}),
    submissionCount: attr('number'),
    mySubmissionCount: attr('number')
});
