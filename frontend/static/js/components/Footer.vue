<template>
  <div class="footer" v-if="!display">
    <div class="footer__list">
      <!--<div class="footer__list_item">Поиск</div>-->
      <!--<span>|</span>-->
      <router-link :to="{ name: 'about' }" class="footer__list_item"> О компании</router-link>
      <span>|</span>
      <div class="footer__list_item">Свяжитесь с нами</div>
      <span>|</span>
      <div class="footer__list_item">Политика доставки</div>
      <span>|</span>
      <router-link :to="{ name: 'faq' }" class="footer__list_item">FAQ</router-link>
      <span>|</span>
      <div class="footer__list_item">Обратная связь</div>
    </div>
    <div class="footer__soc">
      <!--<div class="footer__soc_wrapper">-->
        <!--<span class="footer__soc_h">Подписывайтесь на нас</span>-->
        <!--<div class="footer__soc_list">-->
          <!--<div class="footer__soc_list-item"></div>-->
          <!--<div class="footer__soc_list-item"></div>-->
          <!--<div class="footer__soc_list-item"></div>-->
          <!--<div class="footer__soc_list-item"></div>-->
          <!--<div class="footer__soc_list-item"></div>-->
          <!--<div class="footer__soc_list-item"></div>-->
        <!--</div>-->
      <!--</div>-->
    </div>
    <div class="footer__cop">
      <div class="footer__cop_left">
        © 2017 Classical Conversations Bookstore.  Theme by Clean Themes. Powered by Shopify
      </div>
      <div class="footer__cop_right">
        <img class="footer__cop_right-img" src="../../img/cop1.svg" alt="">
        <img class="footer__cop_right-img" src="../../img/cop2.svg" alt="">
        <img class="footer__cop_right-img" src="../../img/cop4.svg" alt="">
        <img class="footer__cop_right-img" src="../../img/cop3.svg" alt="">
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    name: 'footer',
    data() {
      return {

      }
    },
    computed: {
      display() {
        return this.$route.name === 'order'
      }
    }
  }
</script>
