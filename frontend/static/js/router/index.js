import Vue from 'vue'
import Router from 'vue-router'
import main from '../views/Main.vue'
import catalog from '../views/Product.vue'
import cart from '../views/ProductCart.vue'
import basket from '../views/Basket.vue'
import order from '../views/Order.vue'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'main',
      component: main
    },
    {
      path: '/catalog',
      name: 'catalog',
      component: catalog
    },
    {
      path: '/cart',
      name: 'cart',
      component: cart
    },
    {
      path: '/basket',
      name: 'basket',
      component: basket
    },
    {
      path: '/order',
      name: 'order',
      component: order
    }
  ]
})
