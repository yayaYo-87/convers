<template>
    <div class="order__shiptorg" v-show="next === 3">
        <div class="order__shiptorg_item">
            <div class="order__shiptorg_item-name">Адрес доставки</div>
            <div class="order__shiptorg_item-title">{{ city.administrative_area }}, {{ city.short_readable }}, {{ address }}, {{ index }}</div>
            <div class="order__shiptorg_item-edit" @click="backMethods()">Изменить</div>
        </div>
        <div class="order__shiptorg_item">
            <div class="order__shiptorg_item-name">Адрес доставки</div>
            <div class="order__shiptorg_item-title">{{ city.administrative_area }}, {{ city.short_readable }}, {{ address }}, {{ index }}</div>
            <div class="order__shiptorg_item-edit" @click="backMethods()">Изменить</div>
        </div>
        <div class="order__shiptorg_methods">
            <h3 class="order__shiptorg_methods-title">Способ доставки</h3>
            <div class="order__shiptorg_methods-item">

            </div>
        </div>
        <div class="order__info_button">
            <div @click="backMethods()"  class="order__info_button-return">
                <svg class="order__info_button-svg" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10"><path d="M2 1l1-1 4 4 1 1-1 1-4 4-1-1 4-4"></path></svg>
                Вернуться к методам доставки
            </div>
            <div class="order__info_button-bt">
                <button :disabled="!disabledButton" >Перейти к методу оплаты</button>
            </div>
        </div>
    </div>
</template>

<script>
  import axios from 'axios'
  export default {
    data() {
      return{

      }
    },
    computed: {
      city() {
        return this.$store.state.basket.city
      },
      shiptorOrder() {
        return this.$store.state.basket.shiptor
      },
    },
    methods: {
      backMethods(){
        this.$store.dispatch('validation', {typeValid: 'validation', value: 2})
      },
    }
  }

</script>
