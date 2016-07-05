import Ember from 'ember';
//import EmberValidations from 'ember-validations';

export default Ember.Controller.extend({
//
//  validations: {
//    'model.title': {
//      length: {minimum: 3, maximum: 300, messages: {
//        tooShort: 'Please enter a longer title',
//        tooLong: 'Title exceeds limit of 300 characters'
//      }}
//    },
//    'model.description': {
//      length: {minimum: 6, maximum: 2000, messages: {
//        tooShort: 'Please enter a longer description',
//        tooLong: 'Description exceeds limit of 2000 characters'
//      }}
//    },
//    'model.country': {
//      exclusion: {in: ['-Select a country'], message: 'Please choose a country'}
//    },
//    'model.state': {
//      statecheck: {}
//    },
//    'model.city': {
//      length: {maximum: 100, messages: {
//        tooLong: 'City name is too long'
//      }}
//    },
//    'model.startDate': {
//      datecheck: {}
//    },
//    'model.submissionDate': {
//      datecheck: {}
//    }
//  },
//
//  previewOn: false,
//
//  displayErrors: false,
//
//  kill: true,
//
//  actions: {
//    killConference() {
//      if (this.get('kill')) { this.get('model').destroyRecord(); }
//    },
//    selectCountry(country) {
//      this.set('model.country', country);
//    },
//    create(newMeeting){
//      if (this.get('isValid')) {
//        this.set('kill',false);
//        var router = this;
//          newMeeting.save().then(function(params){
//            router.transitionToRoute('conference.index', params.id).then(function(newRoute) {
//              newRoute.controller.set('visited', true);
//          });
//        });
//      } else {
//        this.set('displayErrors', true);
//        if (this.get('errors.model.title').length > 0) {
//          Ember.$('html, body').animate({
//            scrollTop: Ember.$("#titleScroll").offset().top
//          }, 1000);
//        } else if (this.get('errors.model.description').length > 0) {
//          Ember.$('html, body').animate({
//            scrollTop: Ember.$("#descriptionScroll").offset().top
//          }, 1000);
//        } else if (this.get('errors.model.country').length > 0) {
//          Ember.$('html, body').animate({
//            scrollTop: Ember.$("#countryScroll").offset().top
//          }, 700);
//        } else if (this.get('errors.model.state').length > 0) {
//          Ember.$('html, body').animate({
//            scrollTop: Ember.$("#stateScroll").offset().top
//          }, 700);
//        } else if (this.get('errors.model.city').length > 0) {
//          Ember.$('html, body').animate({
//            scrollTop: Ember.$("#cityScroll").offset().top
//          }, 700);
//        } else if (this.get('errors.model.startDate').length > 0) {
//          Ember.$('html, body').animate({
//            scrollTop: Ember.$("#dateScroll").offset().top
//          }, 300);
//        }
//      }
//    },
//    preview() {
//      if (this.get('isValid')) {
//        this.set('previewOn',true);
//      }
//    },
//    previewOff() {
//      this.set('previewOn',false);
//    }
//  }
});
