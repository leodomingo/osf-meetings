import attr from 'ember-data/attr';
import Model from 'ember-data/model';
<<<<<<< HEAD
import { hasMany, belongsTo } from 'ember-data/relationships';
=======
import { belongsTo, hasMany } from 'ember-data/relationships';
>>>>>>> a3605244e3faa2de63e9017595888900335e165f

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
    mySubmissionCount: attr('number'),
    admin: belongsTo('user')
});
