import DS from 'ember-data';
import Ember from 'ember';

import config from 'ember-get-config';

export default DS.JSONAPIAdapter.extend({
    namespace : '',
    host: config.OSF.apiUrl,

    buildURL(){
        var url = this._super(...arguments);
        if (url.lastIndexOf('/') !== url.length - 1) {
            url += '/';
        }
        return url;
    },
    ajax: function(url, method, hash) {
        hash = hash || {};
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
