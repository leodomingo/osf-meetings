import Ember from 'ember';
import moment from 'moment';


export function dateDisplay(params/*, hash*/) {
    var date = new Date(params[0]);
    return moment(date).format("MM-DD-YYYY")
}

export default Ember.Helper.helper(dateDisplay);
