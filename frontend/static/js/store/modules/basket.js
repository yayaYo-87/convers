import axios from 'axios'

const state = {
  results: []
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