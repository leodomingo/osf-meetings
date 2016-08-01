import Ember from 'ember';

/*
* many Controller variables appear to never be accessed here
* they are setup in the search route after search is complete and the model is available in the store 
*/

export default Ember.Controller.extend({
    query: null, /* Holds the current search query */
    underFive: false, /* For pagination UI : true if there are fewer than 5 pages of results */
    onePage: false, /* For pagination UI : true if there is only one page of results */
    buttonArray: [], /* 
                      * For pagination UI : holds the current page links available
                      * 2 before and 2 after the current page 
                      */
    results: null,    /* holds boolean value of there are any results at all*/
    queryParams: ['q', 'p'], /* query params for search route, hold search query and page number */
    page: 1, /* For pagination UI : holds current page number */
    actions: {
        /*
        *   search()
        *   recieves the searchQuery sent up from the meetings navbar
        *   takes the sent value and sets the query parameter 
        *   transitions to search route with query parameter, setting the model with search results
        */
        search(params) {
            let query = params;
            this.set('query', query);
            this.transitionToRoute('search', {queryParams: {q: query, p: this.page }});
        },
        /*
        *   toPage()
        *   redirects to specific page number in search results
        */
        toPage(pageNum){
            this.transitionToRoute('search', {queryParams: {p: pageNum }});
        }
    }
});
