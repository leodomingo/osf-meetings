import Ember from 'ember';

export default Ember.Route.extend({
    info: false,
    init: function(){
        this.controllerFor('index').set('info', false);
        Ember.$('#submission-instructions').hide();
    },
    model(params) {
        return Ember.RSVP.hash({
            conf : this.store.find('conference', params.conference_id),
            allSubmissions : this.store.query('submission',
                {
                    conference: params.conference_id
                }
            )
        });
    },
    isEqual: function(p1, p2) {
        return (p1 === p2);
    },
    actions: {
        download(uri) {
            var link = document.createElement("a");
            link.download = '';
            link.href = uri;
            link.click();
        },
        toggleInfo() {
            let curInfo = this.controllerFor('index').get('info');
            console.log(curInfo);
            if (curInfo === true){
                Ember.$('#submission-instructions').hide(400);
            }
            else {
                Ember.$('#submission-instructions').show(400);
            }
            this.controllerFor('index').set('info', !curInfo);
        },
    }
});
