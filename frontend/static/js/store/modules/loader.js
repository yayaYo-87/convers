
const state = {
  loader: true
};

// actions
const actions = {
  loader({commit}, value){
    commit('loader', { type: 'loader', items: value.value})
  }
};
// getters
const getters = {

};
// mutations
const mutations = {
  loader(state, {type, items}) {
    state[type] = items
  }
};

export default {
  state,
  getters,
  actions,
  mutations
}