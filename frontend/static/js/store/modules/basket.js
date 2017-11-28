import axios from 'axios'

const state = {
  results: [],
  resultsCart: [],
  phone: '',
  city: '',
  email: '',
  hom: '',
  FirstName:'',
  LastName: '',
  address: '',
  index: '',
  shiptor: [],
  validation: 1,
  comment: ''
};


// actions
const actions = {
  results(state){

    axios.get('/api/cart/')
      .then(
        function (response) {

          state.commit('results', { type: 'results', items: response.data});

        },
        function (error) {
        }
      );
  },
  validation(store, {value, typeValid}){
    store.commit('results', { type: typeValid, items: value})
  }

};
// getters
const getters = {

};
// mutations
const mutations = {
  results(state, {type, items}) {
    state[type] = items
  },
  pushItem(state, {type, items}) {
    state[type] = state[type].concat(items)
  },

};

export default {
  state,
  getters,
  actions,
  mutations
}