<template>
  <div class="main-bar">
    <div class="main-bar_item">
      <h2>О нас</h2>
      <p class="main-bar_text">Добро пожаловать в наш онлайн-книжный магазин! Здесь вы найдете учебную программу для школьников, которая поддерживает ...</p>
      <router-link :to="{ name: 'about' }"  class="main-bar_read"><span>Читать дальше →</span></router-link>
    </div>
    <div class="main-bar_item" v-for="item in resultBanner.left_sliders">
      <img :src='item.cover' alt="cover">
    </div>
    <h2>From the Blog</h2>
    <div class="main-bar_item" v-for="item in resultBlog">
      <img class="main-bar_item-img" :src="item.cover" alt="cover">
      <a href="#" class="main-bar_link">{{ item.name }}</a>
      <p class="main-bar_date">April 25, 2017</p>
      <p class="main-bar_text">Time flies when you are having fun or when you have two children under 2-and-half-years-old. I’m just starting my homeschool...</p>
      <a href="#" class="main-bar_read"><span>Read more →</span></a>
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
    },
    created() {
      this.getBanner()
      this.getBlog()
    }
  }
</script>
