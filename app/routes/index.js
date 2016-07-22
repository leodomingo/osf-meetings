import Ember from 'ember';

export default Ember.Route.extend({
  results: true,
  queryParams: {
    q: {refreshModel: true}
  },
  model(params) {

    let foundConferences = this.store.query('conference', {search:params.q, page: params.p}).then((result) => {
        this.set('results', true);
        this.controllerFor('index').set('results', this.results);
          let meta = result.get('meta');
          if(meta.pagination.count === 0)
          {
            this.set('results', false);
            this.controllerFor('index').set('results', this.results);
          }
          return result;
    });
    //console.log(foundConferences.get('length'));
    return foundConferences;
  },
    actions: {
        create() {
            this.transitionTo('conference.new').then(function(newRoute) {
                newRoute.controller.set('displayErrors', false);
            });
        },
        scrollit() {
            let shift = this.controllerFor('index');
            shift.set('visited', true);
            Ember.$('#indexTop').hide(2000);
        },
        tileView() {
            Ember.$('#tileButton').addClass('disabled');
            Ember.$('#listButton').removeClass('disabled');
            let shift = this.controllerFor('index');
            shift.set('tileview', true);
        },
        listView() {
            Ember.$('#listButton').addClass('disabled');
            Ember.$('#tileButton').removeClass('disabled');
            let shift = this.controllerFor('index');
            shift.set('tileview', false);
        },
        filter(params) {
            let shift = this.controllerFor('index');
            shift.set('query', params);
            this.transitionTo('index', {
                queryParams: {
                    q: params
                }
            });
        },
        search(params) {
            this.transitionTo('search', {
                queryParams: {
                    q: params,
                    p: 1
                }
            });
        }
    }
});
