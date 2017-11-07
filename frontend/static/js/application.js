// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './views/App.vue'
import router from './router/index'

import '../style/global.styl'

Vue.config.productionTip = false
//Плагины
import VueAwesomeSwiper from 'vue-awesome-swiper'
import { swiper, swiperSlide } from 'vue-awesome-swiper'
require('swiper/dist/css/swiper.css')
Vue.use(VueAwesomeSwiper);



/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  swiper,
  swiperSlide,
  template: '<App/>',
  components: { App }
})

