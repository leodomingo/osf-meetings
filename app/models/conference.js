import attr from 'ember-data/attr';
//import Collection from './collection';
import Model from 'ember-data/model';
import { hasMany } from 'ember-data/relationships';
import { validator, buildValidations } from 'ember-cp-validations';

const Validations = buildValidations({
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
    mySubmissionCount: attr('number')
});
