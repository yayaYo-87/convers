<template>
    <div class="order__shiptorg" v-show="next === 2">
        <div class="order__shiptorg_item">
            <div class="order__shiptorg_item-name">Адрес доставки</div>
            <div class="order__shiptorg_item-title">{{ city.administrative_area }}, {{ city.short_readable }}, {{ address }}, {{ index }}</div>
            <div class="order__shiptorg_item-edit" @click="backMethods()">Изменить</div>
        </div>
        <div class="order__shiptorg_methods">
            <h3 class="order__shiptorg_methods-title">Способ доставки</h3>
            <div class="order__shiptorg_methods-item"
                 :class="{ 'order__shiptorg_methods-item-active'  : indexShiptor === index}"
                 @click="shiptorAdd(item, index)"
                 v-for="(item, index) in result.methods">
                <div class="order__shiptorg_methods-item-loader"></div>
                <div class="order__shiptorg_methods-item-title">{{ item.method.name }}, {{ item.method.description }}</div>
                <div class="order__shiptorg_methods-item-total">
                    {{ item.days }}, {{ item.cost.total.sum }}
                    <span class="rubl" > &#8399;</span>
                </div>
            </div>
        </div>
        <div class="order__info_button">
            <div @click="backMethods(1)"  class="order__info_button-return">
                <svg class="order__info_button-svg" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10"><path d="M2 1l1-1 4 4 1 1-1 1-4 4-1-1 4-4"></path></svg>
                Вернуться к информации о покупателе
            </div>
            <div class="order__info_button-bt">
                <button @click="backMethods(3)" :disabled="!disabledButton" >Перейти к методу оплаты</button>
            </div>
        </div>
    </div>
</template>

<script>
  import axios from 'axios'
  export default {
    data() {
      return {
        result: [],
        indexShiptor: -1,
        disabledButton: false,
        shiptor: [

        ]
      }
    },
    computed: {
      next(){
        return this.$store.state.basket.validation
      },
      phone() {
        return this.$store.state.basket.phone
      },
      city() {
        return this.$store.state.basket.city
      },
      email() {
        return this.$store.state.basket.email
      },
      FirstName() {
        return this.$store.state.basket.FirstName
      },
      LastName() {
        return this.$store.state.basket.LastName
      },
      address() {
        return this.$store.state.basket.address
      },
      index() {
        return this.$store.state.basket.index
      },
    },
    watch: {
      next(now) {
        if( now === 2) {
          this.calculateShipping()
        }
      },
      shiptor(now){
        this.disabledButton = true
        this.$store.dispatch('validation', {typeValid: 'shiptor', value: now})
      }
    },
    methods: {
      shiptorAdd(value,index){
        this.indexShiptor = index
        this.shiptor = value
      },
      backMethods(id){
        this.$store.dispatch('validation', {typeValid: 'validation', value: id})
      },
      calculateShipping() {
        const self = this;
        axios.post('/shiptorg/', {
          json: {
            "id": "JsonRpcClient.js",
            "jsonrpc": "2.0",
            "method": "calculateShipping",
            "params": {
              "length": 10,
              "width": 10,
              "height": 10,
              "weight": 2,
              "country_code": "RU",
              "kladr_id": self.city.kladr_id,
            }
          }
        }).then(
          function (response) {

            self.result = response.data.result
          }
        )

      }
    },
    mounted(){

    }
  }
</script>
