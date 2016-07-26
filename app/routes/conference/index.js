import Ember from 'ember';

export default Ember.Route.extend({
    model(params) {
        this.store.adapterFor('submission').set('namespace', `conferences/${params.conference_id}`);
        return Ember.RSVP.hash({
            conf : this.store.find('conference', params.conference_id),
            submissions : this.store.findAll('submission')
        });
    }
});
