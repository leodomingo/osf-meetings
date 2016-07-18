import DS from 'ember-data';
import Ember from 'ember';

export default DS.JSONAPIAdapter.extend({
    host: 'http://localhost:8000',
    buildURL(modelName, id, snapshot, requestType) {
        // Fix issue where CORS request failed on 301s: Ember does not seem to append trailing
        // slash to URLs for single documents, but DRF redirects to force a trailing slash
        var url = this._super(...arguments);
        if (requestType === 'deleteRecord' || requestType === 'updateRecord' || requestType === 'findRecord') {
            if (snapshot.record.get('links.self')) {
                url = snapshot.record.get('links.self');
            }
        }
        if (url.lastIndexOf('/') !== url.length - 1) {
            url += '/';
        }
        return url;
    },
    ajax: function(url, method, hash) {
        hash.crossDomain = true;
        hash.xhrFields = {withCredentials: true};
        return this._super(url, method, hash);
    },
    headers: Ember.computed(function() {
        var csrftoken = "";
        try {
            csrftoken = Ember.get(document.cookie.match(/csrftoken\=([^;]*)/), "1");
        } catch(e){
            console.log(e);
            console.log('no csrftoken present');
        }

        return { "X-CSRFToken": csrftoken };
    }).volatile()
});
