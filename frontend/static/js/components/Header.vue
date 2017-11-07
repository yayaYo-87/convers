<template>
  <div class="header" v-if="!display">
    <div class="header__wrapper">
      <div class="header__logo">
        <img src="../../img/logo.png" alt="">
      </div>
      <div class="header__right">
        <!--<div class="header__right_soc">-->
          <!--<div class="header__right_soc-items">-->
            <!--<div class="header__right_soc-item"></div>-->
            <!--<div class="header__right_soc-item"></div>-->
            <!--<div class="header__right_soc-item"></div>-->
            <!--<div class="header__right_soc-item"></div>-->
            <!--<div class="header__right_soc-item"></div>-->
            <!--<div class="header__right_soc-item"></div>-->
            <!--<div class="header__right_soc-item"></div>-->
          <!--</div>-->
          <!--<div class="header__right_soc-log">-->
            <!--<div class="header__right_soc-log_text"><span>Вход</span>  |</div>-->
            <!--<div class="header__right_soc-log_reg">&nbsp;<span>Регистрация</span></div>-->
          <!--</div>-->
        <!--</div>-->
        <div class="header__right-search">
          <div class="header__right-search_left">
            <input type="text" placeholder="Поиск">
          </div>
          <div class="header__right-search_right">
            <router-link tag="button" :to="{name: 'basket'}" class="button">Корзина <span>(2)</span></router-link>
          </div>
        </div>
      </div>
    </div>
    <div class="header__menu">
      <div class="header__menu_item"><router-link :to="{ name: 'main' }">Главная</router-link></div>
      <div class="header__menu_item header__menu_item-popup">
        <header-menu-item
          :title='"Магазин по программе"'
        ></header-menu-item>
      </div>
      <div class="header__menu_item header__menu_item-popup">
        <header-menu-item
          :title='"Сувениры"'
        ></header-menu-item>
      </div>
      <div class="header__menu_item header__menu_item-popup">
        <header-menu-item
          :title='"Магазин по программе"'
        ></header-menu-item>
      </div>
      <div class="header__menu_item"><a href="#">FAQ</a></div>
      <div class="header__menu_item"><a href="#">О компании</a></div>
      <div class="header__menu_item"><a href="#">Свяжитесь с нами</a></div>
      <div class="header__menu_item"><a href="#">Политика доставки</a></div>
    </div>
  </div>
</template>

<script>
  import headerMenuItem from './HeaderMenuItem.vue'
  export default {
    name: 'HelloWorld',
    data () {
      return {
        msg: 'Welcome to Your Vue.js App'
      }
    },
    components: {
      headerMenuItem
    },
    computed: {
      display() {
        return this.$route.name === 'order'
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->

