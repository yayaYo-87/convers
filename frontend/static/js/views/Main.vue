<template>
  <div class="main">
    <div class="main__banner">
      <div class="main__banner_left">
        <swiper :options="swiperOption">
          <swiper-slide
                  v-for="(item, index) in resultSlider.top_sliders"
                  :key="index">
            <a target="_blank"  :href="item.link"><img :src="item.cover" alt="cover"></a>
          </swiper-slide>
        </swiper>
        <div class="main__banner-prev" slot="button-prev"></div>
        <div class="main__banner-next" slot="button-next"></div>
      </div>
      <div class="main__banner_right">
        <img :src="resultBanner.cover" alt="cover">
      </div>
    </div>
    <div class="main__page">
      <main-bar></main-bar>
      <main-product></main-product>
    </div>
  </div>
</template>

<script>
  import mainBar from '../components/MainBar.vue'
  import mainProduct from '../components/MainProduct.vue'
  import axios from 'axios'

  export default {
    name: 'main',
    components: {
      mainBar,
      mainProduct,

    },
    data() {
      return {
        resultSlider: [],
        resultBanner: [],
        swiperOption: {
          paginationClickable: true,
          nextButton: '.main__banner-next',
          prevButton: '.main__banner-prev',
          grabCursor: true,
          autoplay: 5000,
          speed: 1000,
          loop: true,
          cube: {
            shadow: true,
            slideShadows: true,
            shadowOffset: 20,
            shadowScale: 0.94
          }
        }
      }
    },
    computed: {

    },
    methods: {
      getSlider() {
        const self = this
        axios.get('/api/top_slider/')
          .then(
            function (response) {
              self.resultSlider = response.data.results[0]

            },
            function (error) {

            }
          )
      },
      getBanner() {
        const self = this
        axios.get('/api/top_banner/')
          .then(
            function (response) {
              self.resultBanner = response.data.results[0]

            },
            function (error) {

            }
          )
      },
    },
    created() {
      this.getSlider()
      this.getBanner()
    }
  }
</script>
