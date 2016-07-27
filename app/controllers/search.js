import Ember from 'ember';

export default Ember.Controller.extend({
    query: null,
    underFive: false,
    onePage: false,
    buttonArray: [],
    results: null,
    store: Ember.inject.service('store'),
    queryParams: ['q', 'p'],
    page: 1,
    actions: {
        toPage(pageNum){
            this.transitionToRoute('search', {queryParams: {p: pageNum }});
        }
    }
});
