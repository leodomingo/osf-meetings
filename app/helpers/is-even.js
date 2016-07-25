import Ember from 'ember';

export function isEven(params/*, hash*/) {
	var value = params[0];
	if ((value%2)== 0)
	{
		return true;
	}
  return false;
}

export default Ember.Helper.helper(isEven);
