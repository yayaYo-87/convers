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

require('swiper/dist/css/swiper.css')
Vue.use(VueAwesomeSwiper);
Vue.use(VueResource);

Vue.use(Vue2Filters)

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

