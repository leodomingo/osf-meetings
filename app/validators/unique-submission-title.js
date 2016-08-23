import Ember from 'ember';
import BaseValidator from 'ember-cp-validations/validators/base';

const UniqueSubmissionTitle = BaseValidator.extend({
    store: Ember.inject.service(),

    validate(value/*, options, model, attribute*/) {
        return this.get('store').query('submission', {
            title : value
        }).then(result => {
            return Ember.isEmpty(result) ? true : `This title already exists.`;
        });
    }
});

UniqueSubmissionTitle.reopenClass({
    /**
     * Define attribute specific dependent keys for your validator
     *
     * @param {String}  attribute   The attribute being evaluated
     * @param {Unknown} options     Options passed into your validator
     * @return {Array}
     */
    getDependentsFor(/* attribute, options */) {
        return [];
    }
});

export default UniqueSubmissionTitle;
