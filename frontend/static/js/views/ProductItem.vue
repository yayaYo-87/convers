<template>
    <div class="product">
        <div class="product__header">
            <router-link class="product__header-active"   tag="span" :to="{ name: 'main' }" >Главная</router-link> »
            <span class="product__header-disabled" >  {{result.name }}</span>
        </div>
        <h1 class="product__title">
            {{ result.name }}
        </h1>
        <div class="product__desc" v-html="result.description" >

        </div>
        <div class="product__items">
            <div class="product_item"
                 v-for="item in result.goods_categories"
            >
                <router-link
                        tag="div"
                        :to="{ name: 'cart', params: { id: $route.params.id, item: item.id } }"
                        class="product_item-img"
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
        const id = this.$route.params.id
        axios.get('/api/category/' + id + '/')
          .then(
            function (response) {
              self.result = response.data
            },
            function (error) {

            }
          )
      }
    },
    created() {
      this.get()
    }
  }
</script>
