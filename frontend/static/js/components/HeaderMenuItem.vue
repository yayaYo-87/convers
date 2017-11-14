<template>
  <div class="" @mouseover="hoverTrue()" @mouseleave="hoverFalse()">
    <router-link  :to="{ name:'catalog', params: { id: slug } }">{{title}}</router-link>
    <span>&#187;</span>
    <transition name="popup">
      <div class="header__menu_item-popup_list"  v-show="popup">
        <router-link :to="{ name: 'catalog', params: {id: header.id} }" class="header__menu_item-popup_list-item"
             :key="index"
             v-for="(header, index ) in cart.catalogs"
        >{{ header.name }}</router-link>
      </div>
    </transition>
  </div>
</template>

<script>
  export default {
    props: ['title', 'slug', 'cart'],
    data() {
      return {
        popup: false
      }
    },
    methods: {
      hoverTrue(){
        this.popup = true
      },
      hoverFalse(){
        this.popup = false
      }
    }
  }
</script>
