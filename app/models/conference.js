import attr from 'ember-data/attr';
import Model from 'ember-data/model';
import { validator, buildValidations } from 'ember-cp-validations';
import { belongsTo, hasMany } from 'ember-data/relationships';

var Validations = buildValidations({
    title: {
        description: 'Title',
        validators: [
            validator('presence', true),
            validator('length', {
                min: 4,
                max: 50
            })
        ]
    },
    city: {
        description: 'City',
        validators: [ validator('presence', true) ]
    },
    state: {
        description: 'State',
        validators: [ validator('presence', true) ]
    },
    description: {
        description: 'Conference description',
        validators: [
            validator('presence', true),
            validator('length', {
                min: 20,
                message: 'Description is too short'
            })
        ]
    },
    //This still needs work on date
    //
    //eventStart: validator('presence', true),
    //eventEnd: validator('presence', true),
    //submissionStart: validator('presence', true),
    //submissionEnd: validator('presence', true),
}, {
    debounce: 500
});

export default Model.extend(Validations,{
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
    logo: attr('string', { defaultValue : '' }),
    submissions : hasMany('submission', { async : true }),
    canEdit: attr('boolean', { defaultValue : ''}),
    submissionCount: attr('number'),
    mySubmissionCount: attr('number'),
    admin: belongsTo('user')
});
