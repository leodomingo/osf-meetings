import Ember from 'ember';

import config from '../config/environment';

export default Ember.Component.extend({
    store: Ember.inject.service('store'),
    fixed: true, /* holds status of navbar -> fixed or unfixed <- depending on mobile view or not */
    host: config.providers.osf.host, /* root URL for Osf redirection */
    authenticated: false, /* authentication status */
    user: null, /* current user metadata, initially empty */
    showSearch: false, /* holds current view status of search dropdown */

        /*
        *   init: function()
        *   Initialization sequence for the navbar 
        *   Ajax request to the user endpoint to establish authentication
        *   If authenticated, user metadata is populated, 
        *   if not, then authentication status is set to false
        *
        */

    init: function() {
        this._super(...arguments);
        var self = this;
        Ember.$.ajax({
            url: config.providers.osfMeetings.currentUser,
            dataType: 'json',
            contentType: 'text/plain',
            xhrFields: {
                withCredentials: true,
            }
        }).then(function(loggedIn) {
            if (!(loggedIn.errors)) {
                self.set('authenticated', true);
                self.set('user', loggedIn);
                self.get('store').pushPayload('user', loggedIn);
            }
            else {
                self.set('authenticated', false);
                self.set('user', null);
            }
        });
    },
    actions: {
        /*
        *   search()
        *   search function sends action to route component is nested in,
        *   carries searchQuery parameter with it  
        */
        search: function() {
            this.sendAction('search', this.get("searchQuery"));},

        /*********************************************************/
        /*
        filter: function(){
            console.log('Filtering');
            this.sendAction('filter', this.get("searchQuery"));},
         */
        /*********************************************************/

        /*
        *   logout()
        *   sends action to the application level,
        *   subsequently logs out and removes user metadata
        */
        logout: function() {
            this.sendAction('logout');},
        /*********************************************************/

        /*
        *   logout()
        *   sends action to the application level,
        *   subsequently logs in and adds user metadata
        */
        login: function() {
            this.sendAction('login');},
        /*********************************************************/
        /*
        * unFix()
        * Toggles position status of navbar depending on mobile or desktop view
        */
        unFix: function() {
            if (this.get("fixed") === true){
                 Ember.$('#create').removeClass("navbar-fixed-top");
                 this.set('fixed', false);}
            else{
                Ember.$('#create').addClass("navbar-fixed-top");
                this.set('fixed', true);}
            },
        /*********************************************************/
            /*
            * Toggles view of the dropdown search bar based on search icon click
            */
        toggleSearch: function(){
            if (this.get("showSearch") === false){
                this.set("showSearch", true);}
            else{
                this.set("showSearch", false);}
        }
        /*********************************************************/
    }
});
