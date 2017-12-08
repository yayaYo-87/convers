import Vue from 'vue'
import Router from 'vue-router'


const main = () => import('../views/Main.vue');
const catalog = () => import('../views/Product.vue');
const cart = () => import('../views/ProductCart.vue');
const basket = () => import('../views/Basket.vue');
const order = () => import('../views/Order.vue');
const catalogItem = () => import('../views/ProductItem.vue');
const page = () => import('../views/Page.vue');
const faq = () => import('../views/Faq.vue');
const payment = () => import('../views/Payment.vue');
const support = () => import('../views/Support.vue');

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
      path: '/payment_success',
      name: 'payment_success',
      component: payment
    },
    {
      path: '/support',
      name: 'support',
      component: support
    },
    {
      path: '/payment_error',
      name: 'payment_error',
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
