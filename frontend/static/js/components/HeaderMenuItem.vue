<template>
  <div class="" @mouseover="hoverTrue()" @mouseleave="hoverFalse()">
    <router-link  :to="{ name:'catalog' }">{{title}}</router-link>
    <span>&#187;</span>
    <transition name="popup">
      <div class="header__menu_item-popup_list" v-show="popup">
        <div class="header__menu_item-popup_list-item">Основы</div>
        <div class="header__menu_item-popup_list-item">Ключи </div>
        <div class="header__menu_item-popup_list-item">Вызов Альфа</div>
      </div>
    </transition>
  </div>
</template>

<script>
  export default {
    props: ['title'],
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
