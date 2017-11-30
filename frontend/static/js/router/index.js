import Vue from 'vue'
import Router from 'vue-router'
import main from '../views/Main.vue'
import catalog from '../views/Product.vue'
import cart from '../views/ProductCart.vue'
import basket from '../views/Basket.vue'
import order from '../views/Order.vue'
import catalogItem from '../views/ProductItem.vue'
import page from '../views/Page.vue'
import faq  from '../views/Faq.vue'
import payment from '../views/Payment.vue'

Vue.use(Router)

//При переходе скролит до верха
const scrollBehavior = (to, from, savedPosition) => {
  if (to.hash) {
    console.log(to.hash)
    return {
      selector: to.hash,
    }
  } else {
    return {x: 0, y: 0}
  }
}

export default new Router({
  mode: 'history',
  scrollBehavior,
  routes: [
    {
      path: '/faq',
      name: 'faq',
      component: faq
    },
    {
      path: '/payment',
      name: 'payment',
      component: payment
    },
    {
      path: '/page/:id',
      name: 'page',
      component: page
    },
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
      path: '/item/:item',
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
      path: '/category/:id',
      name: 'catalogItem',
      component: catalogItem
    }
  ]
})
