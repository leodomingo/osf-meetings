import Ember from 'ember';

export default Ember.Route.extend({
  queryParams: {
    q: {refreshModel: true}
  },
  model(params) {
    let foundConferences =  this.store.query('conference', {search:params.q});
    return foundConferences;
  },
  deactivate: function(){
    Ember.$('body').removeClass('hide-scroll');
    Ember.$('html').css({"overflow-y": 'scroll'});
  }
});
