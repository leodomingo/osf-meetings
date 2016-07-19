import Ember from 'ember';

export default Ember.Controller.extend({
  results: null,
  tileview: true,
  queryParams: ['q', 'p'],
  visited: false
});
