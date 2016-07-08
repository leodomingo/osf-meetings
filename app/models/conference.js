import attr from 'ember-data/attr';
//import Collection from './collection';
import Model from 'ember-data/model';

export default Model.extend({
    title: attr('string'),
    city: attr('string'),
    state: attr('string'),
    country: attr('string'),
    start: attr('isodate', { defaultValue : (new Date()).toISOString() }),
    end: attr('isodate', { defaultValue : (new Date()).toISOString() }),
    submissionStart: attr('isodate', { defaultValue : (new Date()).toISOString() }),
    submissionEnd: attr('isodate', { defaultValue : (new Date()).toISOString() }),
    description: attr('string'),
    site: attr('string', { defaultValue : '' }),
    logo: attr('string', { defaultValue : '' }),
});
