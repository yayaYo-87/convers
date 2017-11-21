<template>
  <div class="main_product">
    <h3>Рекомендуемые товары</h3>
    <div class="main_product__items">

      <div class="main_product_item" v-for="item in result">
        <div class="main_product_item-img">
          <router-link :to="{ name: 'cart', params: { item: item.id } }"
                       class="main_product_item-img_wrapper">
            <img class="main_product_item-img_one" :src="item.cover" alt="cover">
            <img class="main_product_item-img_two" :src="item.hover_cover" alt="cover">
          </router-link>
        </div>
        <div class="main_product_item-flex">
          <router-link :to="{ name: 'cart', params: { item: item.id } }"
                       tag="div"
                       class="main_product_item-title">
            <span>{{ item.name }}</span>
          </router-link>
          <div class="main_product_item-bottom">
            <div class="main_product_item-bottom_price">
              {{ item.price }} <span class="rubl"> &#8399;</span>
            </div>
            <router-link tag="button" :to="{ name: 'cart', params: { item: item.id } }" class="main_product_item-bottom_button">
              <span>Подробнее</span>
            </router-link>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
  import axios from 'axios'
  export default {
    name: 'mainProduct',
    data() {
      return {
        result: []
      }
    },
    methods: {
      get() {
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
    },
    created() {
      this.get()
    },
  }
</script>
