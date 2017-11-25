<template>
    <div class="order__shiptorg" v-show="next === 3">
        <div class="order__shiptorg_item order__shiptorg_items">
            <div class="order__shiptorg_pay">
                <div class="order__shiptorg_item-name">Адрес доставки</div>
                <div class="order__shiptorg_item-title">{{ city.administrative_area }}, {{ city.short_readable }}, {{ address }}, {{ index }}</div>
                <div class="order__shiptorg_item-edit" @click="backMethods(1)">Изменить</div>

            </div>
            <div class="order__shiptorg_pay">
                <div class="order__shiptorg_item-name">Метод доставки</div>
                <div class="order__shiptorg_item-title">{{ deliveryMethods }}, {{ deliveryTotal }}</div>
                <div class="order__shiptorg_item-edit" @click="backMethods(2)">Изменить</div>
            </div>
        </div>
        <div class="order__shiptorg_methods">
            <h3 class="order__shiptorg_methods-title">Оплата</h3>

        </div>
        <div class="order__info_button">
            <div @click="backMethods(2)"  class="order__info_button-return">
                <svg class="order__info_button-svg" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10"><path d="M2 1l1-1 4 4 1 1-1 1-4 4-1-1 4-4"></path></svg>
                Вернуться к методам доставки
            </div>
            <div class="order__info_button-bt">
                <button :disabled="!city"  >Оплатить</button>
            </div>
        </div>
    </div>
</template>

<script>
  import axios from 'axios'
  export default {
    data() {
      return{
        deliveryTotal: 0,
        deliveryMethods: '',
      }
    },
    watch: {
      shiptorOrder(now){
        this.deliveryTotal = now.cost.total.sum
        this.deliveryMethods = now.method.name
      }
    },
    computed: {
      next(){
        return this.$store.state.basket.validation
      },
      index() {
        return this.$store.state.basket.index
      },
      address() {
        return this.$store.state.basket.address
      },
      city() {
        return this.$store.state.basket.city
      },
      shiptorOrder() {
        return this.$store.state.basket.shiptor
      },
      shiptorOrder() {
        return this.$store.state.basket.shiptor
      },
    },
    methods: {
      backMethods(id){
        this.$store.dispatch('validation', {typeValid: 'validation', value: id})
      },
    }
  }

</script>
