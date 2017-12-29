// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './views/App.vue'
import router from './router/index'
import store from './store'
import Vue2Filters from 'vue2-filters'
import '../style/global.styl'


Vue.config.productionTip = false
//Плагины
import VueAwesomeSwiper from 'vue-awesome-swiper'
import { swiper, swiperSlide } from 'vue-awesome-swiper'
import VueResource from 'vue-resource'
import * as VueGoogleMaps from 'vue2-google-maps'

require('swiper/dist/css/swiper.css');
Vue.use(VueAwesomeSwiper);
Vue.use(VueResource);

Vue.use(Vue2Filters)
Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyBvWE_sIwKbWkiuJQOf8gSk9qzpO96fhfY',
    libraries: 'places', // This is required if you use the Autocomplete plugin
    // OR: libraries: 'places,drawing'
    // OR: libraries: 'places,drawing,visualization'
    // (as you require)
  }
})
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router: router,
  swiper,
  swiperSlide,
  store,
  template: '<App/>',
  components: { App }
})

