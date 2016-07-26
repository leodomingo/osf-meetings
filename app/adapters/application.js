import OsfAdapter from './osf-adapter';
import Ember from 'ember';

export default OsfAdapter.extend({
    namespace : '',

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
