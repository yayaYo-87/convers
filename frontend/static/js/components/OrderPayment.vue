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
            <!--<h3 class="order__shiptorg_methods-title">Оплата</h3>-->


        </div>
        <div class="order__info_button">
            <div @click="backMethods(2)"  class="order__info_button-return">
                <svg class="order__info_button-svg" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10"><path d="M2 1l1-1 4 4 1 1-1 1-4 4-1-1 4-4"></path></svg>
                Вернуться к методам доставки
            </div>
            <div class="order__info_button-bt">
                <button :disabled="!city && !shiptorOrder"
                        class="tinkoffPayRow"
                        type="submit"
                        @click="initPay()"
                        value="Оплатить">
                    Оплатить
                </button>
            </div>
        </div>
    </div>
</template>

<script>
  import axios from 'axios'
  export default {
    props: ['items'],
    data() {
      return{
        terminalkey: '1505124262290DEMO',
        deliveryTotal: 0,
        deliveryMethods: '',
        result: [],
        Items: [],
        price: 0,
        itemOrder: 0
      }
    },
    watch: {
      shiptorOrder(now){
        this.deliveryTotal = now.cost.total.sum
        this.deliveryMethods = now.method.name
      },
      basket(now){
        this.forEachBasket(now)
      }
    },
    computed: {
      basket() {
        return this.$store.state.basket.results
      },
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
      FirstName() {
        return this.$store.state.basket.FirstName
      },
      LastName() {
        return this.$store.state.basket.LastName
      },
      email() {
        return this.$store.state.basket.email
      },
      phone() {
        return this.$store.state.basket.phone
      },
    },
    methods: {
      forEachBasket(now){
        const self = this
        self.Items = []
        let result = {}
        this.price = now.results[0].price;
        this.itemOrder = now.results[0].id;
        now.results[0].cart_goods.forEach(function (item, i, arr) {

          const items = {
            "Name": item.goods.name,
            "Price": item.goods.price * 100,
            "Quantity": item.count,
            "Amount": item.price * 100,
            "Tax": "none",

          }
          self.Items.push(items)
        })

      },
      backMethods(id){
        this.$store.dispatch('validation', {typeValid: 'validation', value: id})
      },
      initPay() {
        const self = this;
        axios.post('/init_pay/', {
          json: {
            "TerminalKey": self.terminalkey,
            "Amount": self.price * 100 + self.deliveryTotal * 100,
            "OrderId": self.itemOrder,
            "Description": "Классические беседы",
            "DATA": {"Phone": self.phone, "Email": self.email},
            "Receipt": {
              "Email": self.email,
              "Phone": self.phone,
              "Taxation": "usn_income",
              "Items": self.Items
            }
          }
        }).then(
          function (response) {
            console.log(response.data)
            self.result = response.data
            if(response.data.PaymentURL !== undefined){
              location.href = response.data.PaymentURL
            }
          }
        )

      }

    }
  }

</script>
