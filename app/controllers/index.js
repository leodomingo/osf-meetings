import Ember from 'ember';

export default Ember.Controller.extend({
  results: null,
  tileview: true,
  query: null,
  queryParams: ['q', 'p'],
  visited: false,
});
