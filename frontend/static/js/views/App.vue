<template>
  <div class="app" id="app" :class="{'app__wrapper' : order}">
    <header-block></header-block>
    <router-view/>
    <footer-block></footer-block>
  </div>
</template>

<script>
  import headerBlock from '../components/Header.vue'
  import footerBlock from '../components/Footer.vue'

  export default {
    name: 'app',
    components: {
      headerBlock,
      footerBlock
    },
    computed: {
      order(){
        return this.$route.name === 'order'
      }
    }
  }
</script>
