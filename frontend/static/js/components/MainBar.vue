<template>
  <div class="main-bar">
    <div class="main-bar_item" v-for="cart in resultAbout">
      <h2>{{ cart.name }}</h2>
      <p class="main-bar_text" v-html="cart.description"></p>
      <router-link :to="{ name:'page', params: {id: cart.pages.slug} }" class="main-bar_read"><span>Читать дальше →</span></router-link>
    </div>
    <div class="main-bar_item" v-for="item in resultBanner.left_sliders">
      <img :src='item.cover' alt="cover">
    </div>
    <h2>Из блога</h2>
    <div class="main-bar_item" v-for="item in resultBlog">
      <img class="main-bar_item-img" :src="item.cover" alt="cover">
      <a href="#" class="main-bar_link">{{ item.name }}</a>
      <p class="main-bar_date">{{ item.date }}</p>
      <p class="main-bar_text">{{ item.description }}</p>
      <a :href="item.link" class="main-bar_read"><span>Подробнее →</span></a>
    </div>
  </div>
</template>

<script>
  import axios from 'axios'
  export default {
    name: 'mainBar',
    data() {
      return{
        resultBanner: [],
        resultBlog: [],
        resultAbout: [],
      }
    },
    methods:{
      getBanner() {
        const self = this
        axios.get('/api/left_slider/')
          .then(
            function (response) {
              self.resultBanner = response.data.results[0]

            },
            function (error) {

            }
          )
      },
      getBlog() {
        const self = this
        axios.get('/api/left_blog/')
          .then(
            function (response) {
              self.resultBlog = response.data.results

            },
            function (error) {

            }
          )
      },
      getAbout() {
        const self = this
        axios.get('/api/left_about/')
          .then(
            function (response) {
              self.resultAbout = response.data.results

            },
            function (error) {

            }
          )
      },
    },
    created() {
      this.getBanner()
      this.getBlog()
      this.getAbout()
    }
  }
</script>
