import { moduleForComponent, test } from 'ember-qunit';
import hbs from 'htmlbars-inline-precompile';

moduleForComponent('meetings-navbar', 'Integration | Component | meetings navbar', {
  integration: true,
  authenticated: true
});

test('Unauthenticated View', function(assert) {
  // Set any properties with this.set('myProperty', 'value');
  // Handle any actions with this.on('myAction', function(val) { ... });

  this.render(hbs`{{meetings-navbar}}`);

  assert.equal(this.$('.btn-top-signup').text().trim(), 'Sign Up');
  assert.equal(this.$('.btn-top-login').text().trim(), 'Sign In');

});

test('Authenticated View', function(assert) {
	let currentUser =   {
	        "relationships": {
	            "nodes": {
	                "links": {
	                    "related": {
	                        "href": "https://staging-api.osf.io/v2/users/tyxdr/nodes/",
	                        "meta": {}
	                    }
	                }
	            },
	            "institutions": {
	                "links": {
	                    "self": {
	                        "href": "https://staging-api.osf.io/v2/users/tyxdr/relationships/institutions/",
	                        "meta": {}
	                    },
	                    "related": {
	                        "href": "https://staging-api.osf.io/v2/users/tyxdr/institutions/",
	                        "meta": {}
	                    }
	                }
	            },
	            "registrations": {
	                "links": {
	                    "related": {
	                        "href": "https://staging-api.osf.io/v2/users/tyxdr/registrations/",
	                        "meta": {}
	                    }
	                }
	            }
	        },
	        "attributes": {
	            "suffix": "",
	            "personal_website": "",
	            "locale": "en_US",
	            "twitter": "",
	            "linkedin": "",
	            "full_name": "Leandro Alberto Dominguez",
	            "timezone": "America/New_York",
	            "middle_names": "Alberto",
	            "academia_institution": "",
	            "given_name": "Leandro",
	            "impactstory": "",
	            "active": "true",
	            "researcherid": "",
	            "family_name": "Dominguez",
	            "github": "",
	            "academia_profile_id": "",
	            "scholar": "",
	            "baiduscholar": "",
	            "date_registered": "2016-06-15T15:13:56.844000",
	            "orcid": "",
	            "researchgate": ""
	        },
	        "type": "users",
	        "id": "tyxdr",
	        "links": {
	            "self": "https://staging-api.osf.io/v2/users/tyxdr/",
	            "html": "https://staging.osf.io/tyxdr/",
	            "profile_image": "https://secure.gravatar.com/avatar/c31b4ef943aaafc2df4f5b01ade8bcee?d=identicon"
	        }
	};
	this.set('user', currentUser);

	this.render(hbs`{{meetings-navbar authenticated=true user=user}}`);
	this.set('authenticated', 'true');
	assert.equal(this.$('#userDropdown').text().trim(), currentUser.attributes.full_name);

});