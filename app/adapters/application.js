import OsfAdapter from './osf-adapter';

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
});
