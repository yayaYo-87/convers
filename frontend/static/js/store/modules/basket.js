import axios from 'axios'

const state = {
  results: [],
  phone: '',
  city: '',
  email: '',
  FirstName:'',
  LastName: '',
  address: '',
  index: '',

  validation: 1
};

// actions
const actions = {
  results(state){

    axios.get('/api/cart/')
      .then(
        function (response) {

          state.commit('results', { type: 'results', items: response.data})
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

};

export default {
  state,
  getters,
  actions,
  mutations
}