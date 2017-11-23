<template>
    <div class="order__shiptorg" v-show="next === 2">
        <div class="order__shiptorg_item">
            <div class="order__shiptorg_item-name"></div>
            <div class="order__shiptorg_item-title">{{ city }}, {{ address }}, {{ index }}</div>
        </div>

        <div class="order__info_button">
            <div  class="order__info_button-return">
                <svg class="order__info_button-svg" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10"><path d="M2 1l1-1 4 4 1 1-1 1-4 4-1-1 4-4"></path></svg>
                Вернуться к информации о покупателе
            </div>
            <div class="order__info_button-bt">
                <button  @click="nextMethods()">Перейти к методу доставки</button>
            </div>
        </div>
        {{ phone }}
        <button @click="postShiptorg()">shiptorg</button>
        {{ result }}
    </div>
</template>

<script>
  import axios from 'axios'
  export default {
    data() {
      return {
        result: []
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
    methods: {
      postShiptorg() {
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
                    "weight": 10,
                    "cod": 10,
                    "declared_cost": 10,
                    "kladr_id": "01000001000",
                    "courier": "dpd"
                }
            }
      }).then(
          function (response) {
            console.log(response)
            self.result = response.date
          }
        )

      }
    }
  }
</script>
