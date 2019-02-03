import { Factory, faker } from 'ember-cli-mirage';

export default Factory.extend({
  first: faker.name.firstName,
  last: faker.name.lastName,
});
