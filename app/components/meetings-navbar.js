import Ember from 'ember';
import config from 'ember-get-config';
import {
    getAuthUrl
} from 'ember-osf/utils/auth';


export default Ember.Component.extend({
    session: Ember.inject.service(),
    currentUser: Ember.inject.service(),
    onSearchPage: false,
    gravatarUrl: Ember.computed.alias('user.links.profile_image'),
    fullName: null,
    host: config.OSF.url,
    authUrl: "http://localhost:8000/checklogin",
    user: null,
    showSearch: false,

    actions: 
    {
        filter: function()
        {
            this._super(...arguments);
            this._loadCurrentUser();
            this.sendAction('filter', this.get("searchQuery"));
        },
        search: function()
        {
            this.sendAction('search', this.get("searchQuery"));
        }
    }
});
