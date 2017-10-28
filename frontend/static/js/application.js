//js
import Vue from 'vue'
import App from './views/App.vue'
import '../styl/global.styl'
import VueRouter from 'vue-router';
import '../styl/scrollbar.css'
import store from './store'

//Страницы

//Плагины


Vue.use(VueRouter);


//При переходе скролит до верха
const scrollBehavior = (to, from, savedPosition) => {
  if (to.hash) {
    console.log(to.hash)
    return {
      selector: to.hash,
    }
  } else {
    return { x: 0, y: 0 }
  }
};

// const router = new VueRouter({
//   mode: 'history',
//   scrollBehavior,
//   routes:[
//     { path: '/', name: 'index' , component: index},
//     { path: '/service', name: 'services' , component: services},
//     { path: '/service/:id', name: 'servicesItem' , component: servicesItem},
//     { path: '/catalog', name: 'catalog' , component: catalog},
//     { path: '/catalog/:id', name: 'catalogCategory' , component: catalogCategory},
//     { path: '/catalog/:id/:item', name: 'catalogItem' , component: catalogItem},
//     { path: '/project', name: 'project' , component: project},
//     { path: '/project/:id', name: 'projectCategory' , component: projectCategory},
//     { path: '/project/:id/:item', name: 'projectItem' , component: projectItem},
//     { path: '/partners', name: 'partners' , component: partners},
//     { path: '/about', name: 'about' , component: about},
//     { path: '/contacts', name: 'contacts' , component: contacts},
//   ]
// });


new Vue({
  el: '#app',
  components: {
  },
  // router: router,
  store,
  render: h => h(App),

}).$mount('#app');
