import Mirage, {faker} from 'ember-cli-mirage';

export default Mirage.Factory.extend({
	conference: { mySubmissionCount: 2,
				  submissionCount: 5,
				  canEdit: true,
				  logo: 'http://lorempixel.com/640/480',
				  site: 'http://enrico.com',
				  description: 'Voluptatem soluta sed. Totam voluptatem suscipit ab in odio sed. Est quidem necessitatibus quos.',
				  submissionEnd: '2016-12-26T07:32:09.162Z',
				  submissionStart: '2015-10-10T03:01:36.593Z',
				  eventEnd: '2016-12-24T21:58:35.342Z',
				  eventStart: '2015-09-15T00:12:13.454Z',
				  country: 'Latvia',
				  state: 'Louisiana',
				  city: 'North Dewittfort',
				  title: 'Gorczany, O\'Keefe and Abshire',
				  id: '1' },
	title: faker.company.companyName(),
	description: faker.lorem.paragraph(),
	canEdit: true,
	category: faker.lorem.word(),
	nodeId: faker.random.number(),
	dateCreated: faker.date.past(),
	downloadLink: faker.internet.url(),
	downloadCount: faker.random.number()
});
