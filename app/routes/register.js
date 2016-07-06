import Ember from 'ember';
import CheckLoginMixin from 'osf-meetings/mixins/check-login-mixin'

export default Ember.Route.extend(CheckLoginMixin, {
  model() {
    return this.store.createRecord('conference');
  },
  deactivate: function() {
    var controller = this.get('controller');
    controller.send('killConference');
    controller.set('kill',true);
    controller.set('displayErrors',false);
  },
  actions: {
    back() {
      this.transitionTo('index').then(function(newRoute) {
        newRoute.controller.set('visited', true);
      });
    }
  }
});
