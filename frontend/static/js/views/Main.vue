<template>
  <div class="main">
    <div class="main__banner">
      <div class="main__banner_left">
        <swiper :options="swiperOption">
          <swiper-slide><img src="../../img/slide_1_image.jpg" alt=""></swiper-slide>
          <swiper-slide><img src="../../img/slide_2_image.jpg" alt=""></swiper-slide>
          <swiper-slide><img src="../../img/slide_3_image.jpg" alt=""></swiper-slide>
          <swiper-slide><img src="../../img/slide_4_image.jpg" alt=""></swiper-slide>
          <swiper-slide><img src="../../img/slide_5_image.jpg" alt=""></swiper-slide>
        </swiper>
        <div class="main__banner-prev" slot="button-prev"></div>
        <div class="main__banner-next" slot="button-next"></div>
      </div>
      <div class="main__banner_right">
        <img src="../../img/banner_right_image.png" alt="">
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

  export default {
    name: 'main',
    components: {
      mainBar,
      mainProduct
    },
    data() {
      return {
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
  }
</script>
