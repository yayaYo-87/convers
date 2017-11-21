<template>
    <div class="faq__item_cart" :class="{'faq__item_cart-active' : active}" >
        <svg class="faq__item_cart-arrow" style="display: inline;">
            <use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#s4com-icon-arrow-right">
                <svg id="s4com-icon-arrow-right" viewBox="0 0 512 512" width="100%" height="100%">
                    <path d="m154 0l-90 90 181 181-181 181 90 91 272-272z"></path>
                </svg>
            </use>
        </svg>
        <div class="faq__item_cart-name" @click="activePopup()">{{ name }}</div>
        <div class="faq__item_cart-desc" v-show="active">{{ desc }}</div>

    </div>
</template>

<script>
  export default {
    props: ['desc', 'name'],
    data() {
      return {
        active: false
      }
    },
    methods: {
      activePopup () {
        this.active = !this.active
      }
    }
  }
</script>