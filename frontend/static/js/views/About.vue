<template>
    <div class="about">
        <div class="product__header">
            <router-link class='product__header-active' tag="span" :to="{ name: 'main' }" >Главная</router-link> »
            <span class="product__header-disabled" > О нас</span>
        </div>
        <div class="about__wrapper">
            <div class="about__wrapper-left">
                <h1 class="about__title">О нас</h1>
                <h2>Добро пожаловать в наш интернет-магазин!</h2>
                Здесь вы найдете учебную программу для школьников, которая поддерживает сообщество классических бесед десятков тысяч опытных семейных домов, которые продвигают христианскую, классическую, общинную модель домашнего обучения, используя учебную программу классических бесед.
            </div>
            <div class="about__wrapper-right">
                <bar></bar>
            </div>
        </div>
    </div>
</template>

<script>
  import bar from '../components/Bar.vue'

  export default {
    data() {
      return {

      }
    },
    components: {
      bar
    },

  }
</script>