import Ember from 'ember';

export default Ember.Route.extend({
    model() {
        var conference = this.store.findAll('conference');
        conference.forEach(function(item) {
            console.log(item);
        });

        return Ember.RSVP.hash({
            conf : conference
            //I need submissions per conference
            //submissions : this.store.findAll('submission')
        });
    }
//        activate: function() {
//            Ember.$('body').addClass('hide-scroll');
//            Ember.$('html').css({overflow: 'hidden'});
//        },
//        deactivate: function(){
//            Ember.$('body').removeClass('hide-scroll');
//            Ember.$('html').css({"overflow-y": 'scroll'});
//        }
});
