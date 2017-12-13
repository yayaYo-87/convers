<template>
    <div class="order__shiptorg" v-show="next === 2">
        <div class="order__shiptorg_item">
            <div class="order__shiptorg_item-name">Адрес доставки</div>
            <div class="order__shiptorg_item-title">{{ city.administrative_area }}, {{ city.short_readable }}, {{ address }}, {{ index }}</div>
            <div class="order__shiptorg_item-edit" @click="backMethods(1)">Изменить</div>
        </div>
        <div class="order__shiptorg_methods">
            <h3 class="order__shiptorg_methods-title">Способ доставки</h3>
            <div class="order__shiptorg_methods-wr" v-if="loader">
                <img class="order__shiptorg_methods-img" src="/static/img/loader.gif" alt="loader">
            </div>
            <div class="order__shiptorg_methods-item"
                 :class="{ 'order__shiptorg_methods-item-active'  : indexShiptor === index}"
                 v-if="item.method.id !== 16 && item.method.id !== 19 && item.method.id !== 13 && item.method.id !== 68"
                 @click="shiptorAdd(item, index)"
                 v-for="(item, index) in result.methods">
                <div class="order__shiptorg_methods-item-loader"></div>
                <div class="order__shiptorg_methods-item-title">{{ item.method.name }}, {{ item.method.description }}</div>
                <div class="order__shiptorg_methods-item-total">
                    {{ item.days }}, {{ Math.ceil(item.cost.total.sum) }}
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
        <map-block></map-block>
    </div>
</template>

<script>
  import axios from 'axios'
  import jsCookie from 'js-cookie'
  import mapBlock from '../components/OrderMap.vue'

  export default {
    data() {
      return {
        result: [],
        indexShiptor: -1,
        disabledButton: false,
        loader: true,
        shiptor: [

        ]
      }
    },
    components:{
      mapBlock
    },
    computed: {
      deliveryPoint() {
        return this.$store.state.basket.deliveryPoint
      },
      basket() {
        return this.$store.state.basket.results
      },
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
          this.pushItem()

        }
      },
      deliveryPoint(now, old){

        if(now.length !== 0) {
          this.disabledButton = false
        } else {
          this.disabledButton = true
        }
      },
      shiptor(now){
        this.disabledButton = true;
        this.$store.dispatch('validation', {typeValid: 'shiptor', value: now})
      }
    },
    methods: {
      shiptorAdd(value,index){
        this.indexShiptor = index;
        this.shiptor = value;
      },
      backMethods(id){
        this.$store.dispatch('validation', {typeValid: 'validation', value: id})
      },
      pushItem(){
        const self = this
        const itemCart = this.basket.results[0].cart_goods;
        self.$store.commit('results', { type: 'resultsCart', items: []})
        let id = []
        itemCart.forEach(function (item, i, arr) {
          id.push(item.goods.id);
        })

        let width = 0;
        let height = 0;
        let length = 0;
        let weight = 0;

        id.forEach(function (item, id) {
          axios.get('/api/goods/' + item + '/')
            .then(
              function (response) {
                self.$store.commit('pushItem', { type: 'resultsCart', items: response.data})

                if( width <=  response.data.width) {
                  width = response.data.width
                }
                if( length <=  response.data.length) {
                  length = response.data.length
                }

                weight += response.data.weight;
                height += response.data.height;

                if(itemCart.length - 1 === id) {
                  self.calculateShipping(weight, height, length, width)
                }
              }
            )

        })

      },
      calculateShipping(weight, height, length, width) {
        const self = this;
        axios.post('/shiptorg/', {
          json: {
            "id": "JsonRpcClient.js",
            "jsonrpc": "2.0",
            "method": "calculateShipping",
            "params": {
              "length": length,
              "width": width,
              "height": height,
              "weight": weight,
              "country_code": "RU",
              "declared_cost": self.basket.results[0].total_count,
              "kladr_id": self.city.kladr_id,
            }
          }
        }).then(
          function (response) {
            self.loader = false;
            self.result = response.data.result
          }
        )
      }
    },
    mounted(){

    }
  }
</script>
