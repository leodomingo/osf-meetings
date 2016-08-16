import  Ember from 'ember';
import BaseValidator from 'ember-cp-validations/validators/base';

const UniqueIdentifier = BaseValidator.extend({
  store: Ember.inject.service(),

  validate(value, options, model, attribute) {
    if (value){
          return this.get('store').query('conference', {
            id: value,
        }).then((result) => {
            let meta = result.get('meta');
            if (meta.pagination.count !== 0) {
                let message = "The conference identifier \"" +  value + "\" is already in use.";
                return message;
            } else {
              let message = "The conference identifier " +  value + " is available!";
              return true;
            }
        });
      }
    }
});


UniqueIdentifier.reopenClass({
  /**
   * Define attribute specific dependent keys for your validator
   *
   * @param {String}  attribute   The attribute being evaluated
   * @param {Unknown} options     Options passed into your validator
   * @return {Array}
   *
   */
  getDependentsFor(/* attribute, options */) {
    return [];
  }
});

export default UniqueIdentifier;
