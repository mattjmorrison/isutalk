import Route from '@ember/routing/route';

export default Route.extend({
  model(params) {
    return this.store.find('person', params.id);
  },
  actions: {
    edit(person) {
      person.save();
      this.transitionTo('people');
    }
  }
});
