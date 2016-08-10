import Ember from 'ember';

export default Ember.Controller.extend({

    // Validations are currently disabled for developing. They will likely need to be completely 
    // re-implemented. Currently they are set up using the ember-validations library which only
    // works with model variables. However, we have since changed our implementation so that the 
    // model does not exist while the route is loaded, and the model is only generated after the form
    // has been filled out. Because of this, model variables no longer exist on the page. So unless
    // there is a reason to go back to creating the model when the page is loaded, an alternate 
    // validations library will need to be used.

//Code for validations: 
//    displayErrors: false,
//    tagError: false,
//    kill: true,
//
//    validations: {
//        'model.title': {
//            length: {minimum: 3, maximum: 200, messages: {
//                tooShort: 'Please enter a valid title',
//                tooLong: 'Title exceeds limit of 200 characters'
//            }}
//        },
//        //TODO: Validation for contributors?
//        'model.description': {
//            length: {minimum: 6, maximum: 2000, messages: {
//                tooShort: 'Please enter a valid description',
//                tooLong: 'Description exceeds limit of 2000 characters.'
//            }}
//        }
//    },
//
//    actions: {
//        killSubmission() {
//            if (this.get('kill')) {
//                this.get('model').destroyRecord();
//            }
//        },
//        saveNodeSubmission(newNode, id) {
//            if (this.get('isValid')) {
//                this.set('kill',false);
//                newNode.setProperties({
//                    category: 'project',
//                });
//                document.getElementById("fileSubmission").reset();
//                var self = this;
//                newNode.save().then(function() {
//                    self.transitionToRoute('conference.index.index', id);
//                });
//            }
//            else {
//                this.set('displayErrors',true);
//            }
//        }
//    }
});
