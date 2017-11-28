<template>
  <div class="main-bar">
    <div class="main-bar_item">
      <h2>О нас</h2>
      <p class="main-bar_text">Добро пожаловать в наш онлайн-книжный магазин! Здесь вы найдете учебную программу для школьников, которая поддерживает ...</p>
      <a href="#" class="main-bar_read"><span>Читать дальше →</span></a>
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
