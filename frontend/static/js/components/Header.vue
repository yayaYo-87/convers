<template>
  <div class="header" v-if="!display">
    <div class="header__wrapper">
      <router-link :to="{name: 'main'}" tag="div" class="header__logo">
        <img src="../../img/logo.png" alt="">
      </router-link>
      <div class="header__right">
        <div class="header__right_soc">
          <div class="header__right_soc-items">
            <a class="facebook header__right_soc-item" target="_blank" href="https://www.facebook.com/irina.shamolina"></a>
            <a class="vk header__right_soc-item" target="_blank" href="https://vk.com/ishamolina"></a>
            <a class="instagram header__right_soc-item" target="_blank" href="https://instagram.com/irinashamolina "></a>
            <a class="youtube header__right_soc-item" target="_blank" href="https://www.youtube.com/channel/UC1LSsHHVzGkeNdHOdoKyDzw"></a>

          </div>
        </div>
        <div class="header__right-search">
          <!--<div class="header__right-search_left">-->
          <!--<input type="text" placeholder="Поиск">-->
          <!--</div>-->
          <div class="header__right-search_right">
            <router-link tag="button" :to="{name: 'basket'}" class="button"> <span v-for='item in basket'>Корзина ({{ item.total_count }})</span></router-link>
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

      <div class="header__menu_item" v-for="item in resultPage">
        <router-link :to="{ name: 'page', params: { id: item.slug }}">{{ item.name }}</router-link>
      </div>
      <!--<div class="header__menu_item"><a href="#">Политика доставки</a></div>-->
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
        result: [],
        resultPage: []
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
      getPage() {
        const self = this
        axios.get('/api/pages/')
          .then(
            function (response) {
              self.resultPage = response.data.results

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
      this.getPage()
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->

