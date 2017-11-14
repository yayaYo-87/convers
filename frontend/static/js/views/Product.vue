<template>
  <div class="product">
    <div class="product__header">
      <router-link tag="span" :to="{ name: 'main' }" >Главная</router-link> »
      <router-link tag="span" :to="{ name: 'main' }" >  {{result.name }}</router-link>
    </div>
    <h1 class="product__title">
      {{result.name}}
    </h1>
    <div class="product__items"
         v-if=" result.catalogs && result.catalogs.length !== 0"
         v-for="items in result.catalogs"

    >
      <div class="product_item"
           v-for="item in items.goods_categories"
      >
        <router-link
                tag="div"
                :to="{ name: 'cart', params: { id: $route.params.id, item: item.id } }"
                class="product_item-img "
                :class="{'product_item-img-hover' : item.hover_cover }"
        >
          <div class="product_item-img_wrapper">
            <img  class="product_item-img_one" :src=" item.cover " alt="">
            <img class="product_item-img_two" :src=" item.hover_cover " alt="">
          </div>
        </router-link>
        <div class="product_item-flex">
          <div class="product_item-title">
            <span>{{ item.name }}</span>
          </div>
          <div class="product_item-bottom">
            <div class="product_item-bottom_price">
              ${{ item.price }}
            </div>
            <button class="product_item-bottom_button">
              <router-link
                tag="span"
                :to="{ name: 'cart', params: { id: $route.params.id, item: item.id } }"
              >
                Подробнее
              </router-link>
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import axios from 'axios'

  export default {
    data() {
      return {
        result: []
      }
    },
    watch: {
      '$route.params' : 'get'
    },
    methods: {
      get() {
        const self = this
        axios.get('/api/catalog/')
          .then(
            function (response) {
              const catalog = response.data
              catalog.forEach( function (item, i, arr) {
                const id = self.$route.params.id
                if(id === item.slug) {
                  self.result = item
                }
              })

            },
            function (error) {

            }
          )
      }
    },
    mounted() {
      this.get()
    }
  }
</script>
