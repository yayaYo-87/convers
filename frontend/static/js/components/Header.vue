<template>
  <div class="header" v-if="!display">
    <div class="header__wrapper">
      <router-link :to="{name: 'main'}" tag="div" class="header__logo">
        <img src="../../img/logo.png" alt="">
      </router-link>
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
          <!--<div class="header__right-search_left">-->
            <!--<input type="text" placeholder="Поиск">-->
          <!--</div>-->
          <div class="header__right-search_right">
            <router-link tag="button" :to="{name: 'basket'}" class="button">Корзина <span v-for='item in basket'>({{ item.total_count }})</span></router-link>
          </div>

        </div>
      </div>
    </div>
    <div class="header__menu">
      <div class="header__menu_item"><router-link :to="{ name: 'main' }">Главная</router-link></div>
      <div class="header__menu_item header__menu_item-popup"
           v-for="(item, index) in result "
           :key="index"
      >
        <header-menu-item
                :cart="item"
                :slug="item.slug"
        ></header-menu-item>
      </div>
      <div class="header__menu_item"><router-link :to="{ name: 'faq' }">FAQ</router-link></div>
      <div class="header__menu_item"><router-link :to="{ name: 'about' }">О компании</router-link></div>
      <div class="header__menu_item"><a href="#">Свяжитесь с нами</a></div>
      <div class="header__menu_item"><a href="#">Политика доставки</a></div>
    </div>
  </div>
</template>

<script>
  import headerMenuItem from './HeaderMenuItem.vue'
  import axios from 'axios'

  export default {
    name: 'header',
    data () {
      return {
        result: []
      }
    },
    components: {
      headerMenuItem
    },
    computed: {
      display() {
        return this.$route.name === 'order'
      },
      basket() {
        return this.$store.state.basket.results.results
      }
    },
    methods: {
      get() {
        const self = this
        axios.get('/api/catalog/')
          .then(
            function (response) {
              self.result = response.data.results

            },
            function (error) {
              console.log(erorr)
            }
          )
      },
      getBasket() {
        this.$store.dispatch('results')
      }
    },
    created() {
      this.get()
      this.getBasket()
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->

