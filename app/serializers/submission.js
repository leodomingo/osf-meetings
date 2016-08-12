import JSONAPISerializer from 'ember-data/serializers/json-api';

export default JSONAPISerializer.extend({
    serialize: function(snapshot, options) {
        // Restore relationships to serialized data
        var serialized = this._super(snapshot, options);

        if(snapshot.record.get('contributor').get('id') !== undefined) {
            serialized.data.relationships = {
                contributor: {
                    data: {
                        id: snapshot.record.get('contributor').get('id'),
                        type: 'Users'
                    }
                }
            };
        }
        return serialized;
    }
});
