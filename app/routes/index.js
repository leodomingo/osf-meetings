import Ember from 'ember';

export default Ember.Route.extend({
//    model() {
//        var conference = this.store.findAll('conference');
//        conference.forEach(function(item) {
//            console.log(item);
//        });
//
//        return Ember.RSVP.hash({
//            conf : conference
//            //I need submissions per conference
//            //submissions : this.store.findAll('submission')
//        });
//    }
//    COME BACK TO THIS for pulling all conferences with length

  results: true,
  queryParams: {
    q: {refreshModel: true}
  },
  model(params) {

    let foundConferences = this.store.query('conference', {search:params.q, page: params.p}).then((result) => {
        this.set('results', true);
        this.controllerFor('index').set('results', this.results);
          let meta = result.get('meta');
          if(meta.pagination.count === 0)
          {
            this.set('results', false);
            this.controllerFor('index').set('results', this.results);
          }
          return result;
    });

    //console.log(foundConferences.get('length'));
    return foundConferences;
  },
  deactivate: function(){
    Ember.$('body').removeClass('hide-scroll');
    Ember.$('html').css({"overflow-y": 'scroll'});
  }
});
