import Mirage, {faker} from 'ember-cli-mirage';

export default Mirage.Factory.extend({
  title: faker.company.companyName(),
  city:  faker.address.city(),
  state: faker.address.state(),
  country: faker.address.country(),
  eventStart: faker.date.past(),
  eventEnd: faker.date.future(),
  submissionStart: faker.date.past(),
  submissionEnd: faker.date.future(),
  description: faker.lorem.paragraph(),
  site: faker.internet.url(),
  logo: faker.image.imageUrl(),
  canEdit: true, 
  submissionCount: 5,
  mySubmissionCount: 2
});