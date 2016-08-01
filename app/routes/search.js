import Ember from 'ember';

export default Ember.Route.extend({
    page: null, /* holds current page number */
    pages: null, /* holds total number of pages in results */
    results: null, /* true if there are any results at all */
    queryParams: {  /* refresh model connects the model hook to a change in the query parameter */
        q: {
            refreshModel: true 
        },
        p: {
            refreshModel: true
        }
    },
    model: function(params) {
        this.controllerFor('search').set('query', params.q); /* sets current query in controller */
        let foundConferences = this.store.query('conference', {  /* queries search endpoint */
            search: params.q,
            page: params.p
        }).then((result) => {
            this.set('results', true);    /* sets results variable in controller */
            let meta = result.get('meta'); /* gets request metadata and sets pagination variables */
            this.set('pages', meta.pagination.pages);
            this.set('page', meta.pagination.page);
            if (meta.pagination.count === 0) {
                this.set('results', false);
            }
            return result;
        });
        return foundConferences;
    },
    setupController: function(controller, model) {
        /*
        *   sets controller variables for pagination
        *   creates pagination button array based on results pages
        */
        let page = this.get('page');
        let pages = this.get('pages');
        let push = this.controllerFor('search');
        push.set('buttonArray', null);
        if (pages === 1) {
            push.set('onePage', true);
        } else {
            push.set('onePage', false);
        }
        this._super(controller, model);
        push.set('results', this.get('results'));
        if ((pages > 1) && (pages < 5)) {
            let buttonArray = [];
            let i = 1;
            while (i <= pages) {
                buttonArray.push(i);
                i++;
            }
            push.set('underFive', true);
            push.set('buttonArray', buttonArray);
        } else if ((page <= 3) && (pages > 5)) {
            push.set('buttonArray', [2, 3, 4, 5, 6]);
        } else if ((page > 3) && (page < (pages - 2))) {
            push.set('buttonArray', [page - 2, page - 1, page, page + 1, page + 2]);
        } else if (page >= (pages - 2)) {
            push.set('buttonArray', [pages - 5, pages - 4, pages - 3, pages - 2, pages - 1]);
        }
    }
});
