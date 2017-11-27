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
                        @click="postOrder()"
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
        itemOrder: 0,
        itemsShiptor: []
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
      comment() {
        return this.$store.state.basket.comment
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
      hom() {
        return this.$store.state.basket.hom
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
      errorPopup(now){
        const newDiv = document.createElement('div')
        newDiv.classList.add('popup')
        newDiv.innerHTML = now

        document.body.appendChild(newDiv)

        setTimeout(function () {
          document.body.removeChild(newDiv)
        }, 6000)
      },
      forEachBasket(now){
        const self = this
        self.Items = []
        self.itemsShiptor = []
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
          const itemsShiptor = {
            "shopArticle": item.goods.id,
            "count": item.count,
            "vat": 18,

          }
          self.Items.push(items)
          self.itemsShiptor.push(itemsShiptor)
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
            self.result = response.data
            console.log(response.data)
            if(response.data.ErrorCode === '8') {
              self.errorPopup(response.data.Details)

            }
            if(response.data.PaymentURL !== undefined){
              location.href = response.data.PaymentURL
            }
          }, function (error) {
          }
        )

      },
      shiptor() {
        const self = this;
        const photo = self.resultsCart

        axios.post('/shiptorg/', {
          json: {
            "id": "JsonRpcClient.js",
            "jsonrpc": "2.0",
            "method": "addPackage",
            "params": {
              "stock": 1,
              "length": 10,
              "width": 10,
              "height": 10,
              "weight": 10,
              "cod": 0,
              "external_id": self.basket.results[0].id,
              "departure": {
                "shipping_method": self.shiptorOrder.method.id,
                "delivery_point": null,
                "cashless_payment": true,
                "comment": self.basket.comment,
                "address": {
                  "country": self.city.country.code,
                  "receiver": self.LastName + '' + self.FirstName,
                  "email": self.email,
                  "phone": self.phone,
                  "postal_code": self.index,
                  "administrative_area": self.city.administrative_area,
                  "settlement": self.city.name,
                  "house": self.hom,
                  "address_line_1": self.city.readable_parents + ', ' + self.address + ', ' + self.hom,
                  "kladr_id": self.city.country.kladr_id
                }
              },
              "products": [
                {
                  "shopArticle": "HOLOD10",
                  "count": 1,
                  "price": 15000,
                }
              ]
            }
          }
        }).then(
          function (response) {
            self.initPay()
          }, function (error) {
          }
        )

      },
      postOrder() {
        let self = this
        axios.post('/api/order/', {
          "total_count": self.basket.results[0].total_count,
          "order_delivery": self.shiptorOrder.method.courier,
          "email": self.email,
          "city": self.city.short_readable,
          "index": self.index,
          "address": self.address,
          "first_name": self.FirstName,
          "last_name": self.LastName,
          "phone": self.phone,
          "home": self.hom,
          "total": self.basket.results[0].price + self.shiptorOrder.cost.total.sum
        }).then(

          function (response) {
//
            self.shiptor()
            console.log(response.data)

          }
        )
      }


    }
  }

</script>
