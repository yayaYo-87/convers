<template>
  <div class="footer" v-if="!display">
    <div class="footer__list">

      <div v-for="item in resultPage">
        <span>|</span>
        <router-link

                class="footer__list_item"
                :to="{ name: 'page', params: { id: item.slug }}"
        >{{ item.name }}
        </router-link>
      </div>


      <span>|</span>
      <router-link :to="{ name: 'faq' }" class="footer__list_item">FAQ</router-link>
      <span>|</span>

      <!--<div class="footer__list_item">Обратная связь</div>-->
    </div>
    <div class="footer__soc">
      <div class="header__right_soc">
        Подписывайтесь на нас
        <div class="header__right_soc-items">
          <a class="facebook header__right_soc-item" target="_blank" href="https://www.facebook.com/irina.shamolina"></a>
          <a class="vk header__right_soc-item" target="_blank" href="https://vk.com/ishamolina"></a>
          <a class="instagram header__right_soc-item" target="_blank" href="https://instagram.com/irinashamolina "></a>
          <a class="youtube header__right_soc-item" target="_blank" href="https://www.youtube.com/channel/UC1LSsHHVzGkeNdHOdoKyDzw"></a>
        </div>
      </div>
    </div>
    <div class="footer__cop">
      <div class="footer__cop_left">
        © 2017 «Классические беседы»
      </div>
      <div class="footer__cop_right">
        <img class="footer__cop_right-img" src="../../img/cop1.svg" alt="">
        <img class="footer__cop_right-img" src="../../img/cop2.svg" alt="">
        <img class="footer__cop_right-img" src="../../img/cop4.svg" alt="">
        <img class="footer__cop_right-img" src="../../img/cop3.svg" alt="">
      </div>
    </div>
  </div>
</template>

<script>
  import axios from 'axios'
  export default {
    name: 'footer',
    data() {
      return {
        resultPage: []
      }
    },
    computed: {
      display() {
        return this.$route.name === 'order'
      }
    },
    methods:{
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
      }
    },
    created() {
      this.getPage()
    }
  }
</script>
