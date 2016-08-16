import attr from 'ember-data/attr';
import Model from 'ember-data/model';
import { validator, buildValidations } from 'ember-cp-validations';
import { belongsTo, hasMany } from 'ember-data/relationships';

const Validations = buildValidations({
    id: [
        validator('unique-identifier', {}),
        validator('length', {
            max: 10,
            description: "Conference Identifier",
            message: "Conference Identifier must be fewer than 10 characters"
        })
    ],
    title: validator('presence', {
        presence: true,
        description: 'Conference Title',
        message: 'Title cannot be blank'
     }),
    city: validator('presence', {
        presence: true,
        description: 'Conference City'
    }),
    state: validator('presence', {
        presence: true,
        description: 'Conference State'
    }),
    description: [
        validator('presence', {
            presence: true,
            message: 'Conference description can\'t be blank'
        }),
        validator('length', {
            min: 30,
            description: 'Conference Description',
            message: 'Description is too short'
        })
    ],
    eventStart: validator('presence', true),
    eventEnd: validator('presence', true),
    submissionStart: validator('presence', true),
    submissionEnd: validator('presence', true),
    
});

export default Model.extend(Validations, {
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
