import Vue from 'vue'
import Router from 'vue-router'
import main from '../views/Main.vue'
import catalog from '../views/Product.vue'
import cart from '../views/ProductCart.vue'
import basket from '../views/Basket.vue'
import order from '../views/Order.vue'
import catalogItem from '../views/ProductItem.vue'
Vue.use(Router)

//При переходе скролит до верха
const scrollBehavior = (to, from, savedPosition) => {
  if (to.name === 'item') {
    return { x: 0, y: 0 }
  }
};

export default new Router({
  mode: 'history',
  scrollBehavior,
  routes: [
    {
      path: '/',
      name: 'main',
      component: main
    },
    {
      path: '/catalog/:id',
      name: 'catalog',
      component: catalog
    },
    {
      path: '/catalog/:id/:item',
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
    },
    {
      path: '/catalogItem/:id',
      name: 'catalogItem',
      component: catalogItem
    }
  ]
})
