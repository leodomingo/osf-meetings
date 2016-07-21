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
    _loadCurrentUser() {
        console.log("LoadCurrentUser");
        this.get('currentUser').load().then((user) => this.set('user', user));
        console.log(this.get('user'));
    },
    init: function() {
        this._super(...arguments);
        console.log("INIT");
        console.log(this.get('authUrl'));
        this._loadCurrentUser();
    },
    didUpdateAttrs: function() 
    {
        this._super(...arguments);
        console.log("INIT");
        if (this.get('session.isAuthenticated')) {
            this._loadCurrentUser();
        }
    },
    // TODO: Make these parameters configurable from... somewhere. (currently set by OSF settings module)
    allowLogin: true,
    enableInstitutions: true,

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
