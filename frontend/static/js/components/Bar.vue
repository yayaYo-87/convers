<template>
    <div class="bar">
        <div class="bar__item" v-for="item in resultBanner.left_sliders">
            <a :href="item.link">
                <img :src="item.cover" alt="cover">
            </a>
        </div>
    </div>
</template>

<script>
  import axios from 'axios'
  export default {
    data() {
      return {
        resultBanner: []
      }
    },
    methods: {
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
    },
    created() {
      this.getBanner()
    }
  }
</script>