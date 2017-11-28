<template>
    <div class="about">
        <div class="product__header">
            <router-link class='product__header-active' tag="span" :to="{ name: 'main' }" >Главная</router-link> »
            <span class="product__header-disabled" > О нас</span>
        </div>
        <div class="about__wrapper">
            <div class="about__wrapper-left">
                <h1 class="about__title">{{ resultPage.name }}</h1>

                <div v-html="resultPage.description"></div>

                <h3>Рекомендуемые товары</h3>
                <div class="cart__rew">
                    <div class="cart__item cart__item-width" v-for="item in limitBy(result, 3)">
                        <router-link
                                tag="div"
                                :to="{ name: 'cart', params: {  item: item.id } }"
                                class="cart__item-img"
                                :class="{'cart__item-img-hover' : item.hover_cover }"
                        >
                            <div class="cart__item-img_wrapper">
                                <img class="cart__item-img_one" :src="item.cover" alt="cover">
                                <img class="cart__item-img_two" :src="item.hover_cover" alt="cover">
                            </div>
                        </router-link>
                        <div class="cart__item-flex">
                            <div class="cart__product_item-title">
                                <span>{{ item.name }}</span>
                            </div>
                            <div class="cart__item-bottom">
                                <div class="cart__item-bottom_price">
                                    {{ item.price }}<span class="rubl" > &#8399;</span>
                                </div>
                                <router-link
                                        tag="button"
                                        :to="{ name: 'cart', params: {  item: item.id } }"
                                        class="cart__item-bottom_button">
                                    <span>Подробнее</span>
                                </router-link>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div class="about__wrapper-right">
                <bar></bar>
            </div>
        </div>
    </div>
</template>

<script>
  import bar from '../components/Bar.vue'
  import axios from 'axios'

  export default {
    data() {
      return {
        result: [],
        resultPage: []
      }
    },
    components: {
      bar
    },
    watch: {
      '$route.params.id': 'getPage'
    },
    methods: {
      getRecommend() {
        const self = this;
        axios.get('/api/main_goods/')
          .then(
            function (response) {
              self.result = response.data.results
            },
            function (error) {

            }
          )
      },
      getPage() {
        const self = this;
        const id = this.$route.params.id
        axios.get('/api/pages/' + id + '/')
          .then(
            function (response) {
              self.resultPage = response.data
            },
            function (error) {

            }
          )
      },
    },
    created(){
      this.getRecommend()
      this.getPage()
    }
  }
</script>