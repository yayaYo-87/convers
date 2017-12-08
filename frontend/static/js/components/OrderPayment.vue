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
                <div class="order__shiptorg_item-title">{{ deliveryMethods }}, {{ Math.ceil(deliveryTotal) }}</div>
                <div class="order__shiptorg_item-edit" @click="backMethods(2)">Изменить</div>
            </div>
        </div>
        <div class="order__shiptorg_methods">
            <div class="order__shiptorg_methods-wr" v-if="loader">
                <img class="order__shiptorg_methods-img" src="/static/img/loader.gif" alt="loader">
            </div>
        </div>
        <div class="order__info_button">
            <div @click="backMethods(2)"  class="order__info_button-return">
                <svg class="order__info_button-svg" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10"><path d="M2 1l1-1 4 4 1 1-1 1-4 4-1-1 4-4"></path></svg>
                Вернуться к методам доставки
            </div>
            <div class="order__info_button-bt">
                <button :disabled="disabledR"
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
        disabledR: false,
        terminalkey: '1511862369151DEMO',
        loader: false,
        deliveryTotal: 0,
        deliveryMethods: '',
        result: [],
        Items: [],
        ItemsDelivery: [],
        price: 0,
        itemOrder: 0,
        itemsShiptor: []
      }
    },
    watch: {
      price(now){
        if(now === 0){
          this.disabledR = true
        } else {
          this.disabledR = false
        }
      },
      shiptorOrder(now){
        this.deliveryTotal = now.cost.total.sum
        this.deliveryMethods = now.method.name

        this.ItemsDelivery = {
          "Name": 'Доставка',
          "Price": Math.round(this.shiptorOrder.cost.total.sum * 100),
          "Quantity": 1,
          "Amount": Math.round(this.shiptorOrder.cost.total.sum * 100),
          "Tax": "none",
        };

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
      apartment() {
        return this.$store.state.basket.apartment
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
        }, 3000)
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
          };
          const itemsShiptor = {
            "shopArticle": item.goods.id,
            "count": item.count,
            "vat": 18,

          };
          self.Items.push(items);
          self.itemsShiptor.push(itemsShiptor)
        })
      },
      backMethods(id){
        this.$store.dispatch('validation', {typeValid: 'validation', value: id})
      },
      initPay(id) {
        const self = this;
        axios.post('/init_pay/', {
          id: id
        }).then(
          function (response) {
            if(response.data.ErrorCode === '8') {
              self.errorPopup(response.data.Details)
            }
            if(response.data.PaymentURL !== undefined){
              location.href = response.data.PaymentURL
            }
          }, function (error) {
            self.loader = false

          }
        )

      },
      shiptorPost(id) {
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
              "declared_cost": self.basket.results[0].price,
              "departure": {
                "shipping_method": self.shiptorOrder.method.id,
                "delivery_point": self.city.country.kladr_id,
                "cashless_payment": true,
                "comment": self.basket.comment,
                "address": {
                  "country": self.city.country.code,
                  "receiver": self.LastName + ' ' + self.FirstName,
                  "email": self.email,
                  "phone": self.phone,
                  "postal_code": self.index,
                  "administrative_area": self.city.administrative_area,
                  "settlement": self.city.name,
                  "house": self.hom,
                  "apartment": self.apartment,
                  "address_line_1": self.city.readable_parents + ', ' + self.address + ', дом.' + self.hom + ', ул.' + self.apartment,
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

          }, function (error) {
            self.loader = false
          }
        )

      },
      postOrder() {
        let self = this;
        if ( this.price !== 0 ) {
          this.loader = true;
          this.disabledR = true;
          let self = this;

          this.Items.push(this.ItemsDelivery);
          axios.post('/api/order/', {
            "total_count": self.basket.results[0].total_count,
            "order_delivery": self.shiptorOrder.method.courier,
            "total_delivery": Math.ceil(self.shiptorOrder.cost.total.sum),
            "shipping_id": self.shiptorOrder.method.id,
            "delivery_point": self.city.kladr_id,
            "administrative_area": self.city.administrative_area,
            "email": self.email,
            "apartment": self.apartment,
            "settlement": self.city.name,
            "kladr_id": self.city.kladr_id,
            "city": self.city.short_readable,
            "index": self.index,
            "comment": self.comment,
            "address": self.address,
            "first_name": self.FirstName,
            "last_name": self.LastName,
            "phone": self.phone,
            "home": self.hom,
            "total": parseInt(self.basket.results[0].price + self.shiptorOrder.cost.total.sum)
          }).then(
            function (response) {
//            self.$store.dispatch('results')
              self.initPay(response.data.id)

            }, function (error) {
              self.loader = false
            }
          )
        } else {
          self.errorPopup('Пустая корзина. Добавьте товар!')
        }
      }


    }
  }

</script>
