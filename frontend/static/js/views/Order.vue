<template>
  <div class="order">
    <div class="order__left">
      <div class="order__header">

        <router-link :to="{name: 'main'}" class="">
          <img alt="Classical Conversations Bookstore" class="order__header_logo" src="../../img/logo.png">
        </router-link>

        <div class="order__header_list ">
          <div class="order__header_list-item order__header_list-complited">
            <router-link :to="{name: 'basket'}" class="order__header_list-link">Корзина</router-link>
            <svg class="order__svg order__svg-active" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10"><path d="M2 1l1-1 4 4 1 1-1 1-4 4-1-1 4-4"></path></svg>
          </div>
          <div class="order__header_list-item " :class="{ 'order__header_list-complited': next === 2 || next === 3 }">
            <span class="order__header_list-link" @click="backMethods(1)">Информация о покупателе</span>
            <svg class="order__svg order__svg-active" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10"><path d="M2 1l1-1 4 4 1 1-1 1-4 4-1-1 4-4"></path></svg>
          </div>
          <div class="order__header_list-item"  :class="{'order__header_list-default': next === 1, 'order__header_list-complited': next === 3}">
            <span class="order__header_list-link">Способ доставки</span>
            <svg class="order__svg order__svg-active" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10"><path d="M2 1l1-1 4 4 1 1-1 1-4 4-1-1 4-4"></path></svg>
          </div>
          <div class="order__header_list-item" :class="{'order__header_list-default': next !== 3}">
            <span class="order__header_list-link">Способ оплаты</span>
          </div>
        </div>

      </div>


      <div class="order__info">

        <order-info

        ></order-info>

        <order-shiptorg

        ></order-shiptorg>

        <order-payment

        ></order-payment>

        <div class="order__info_cop">
          <div class="order__info_cop-item">
            Политика возврата
          </div>
          <div class="order__info_cop-item">
            Политика доставки
          </div>
          <div class="order__info_cop-item">
            Политика конфиденциальности
          </div>
        </div>
      </div>
    </div>
    <div class="order__right">
      <div class="order__right_items"v-for="cart in basket.results ">
        <div class="order__right_item"

             v-for="item in cart.cart_goods"
             v-if="item.active"
        >
          <!--<div class="order__right_item-close" @click="switchItem(item.id, 'deactivate')"></div>-->
          <!--<div class="order__right_item-active" v-if="!item.active">-->
          <!--<button class=" button-basket" @click="switchItem(item.id, 'activate')">-->
          <!--<span>Вернуть обратно</span>-->
          <!--</button>-->
          <!--</div>-->
          <div class="order__right_item-img">
            <div class="order__right_item-img_wrapper">
              <img :src="item.goods.cover" alt="cover">
            </div>
            <div class="order__right_item-count">{{item.count}}</div>
          </div>
          <div class="order__right_item-name">{{ item.goods.name }}</div>
          <div class="order__right_item-price">
            {{ item.price }}
            <span class="rubl" > &#8399;</span>
          </div>
        </div>
      </div>
      <div class="order__right_code">
        <div class="order__info_input">
          <label for="code" class="order__info_input-label"
                 :class="{'order__info_input-label_active': focusedCode}"
          >Подарочная карта или код скидки</label>
          <input  @focus="focusedCode = true"
                  @blur="fcCode()"
                  v-model="promocode" id="code"
                  type="text"
                  class="order__info_input-email">
        </div>
        <div class="order__right_code-button">
          <button @click="checkedCode()">Использовать</button>
        </div>
      </div>
      <div class="order__right_subtotal">
        <div class="order__right_subtotal-items">
          <div class="order__right_subtotal-text">Промежуточный итог</div>
          <div class="order__right_subtotal-price" v-for="item in basket.results">{{ item.price }}<span class="rubl" > &#8399;</span></div>
        </div>
        <div class="order__right_subtotal-items" v-if="item.total_discount !== 0" v-for="item in basket.results">
          <div class="order__right_subtotal-text">Скидка по промокоду</div>
          <div class="order__right_subtotal-price" v-for="item in basket.results">{{ item.total_discount }}<span class="rubl" > &#8399;</span></div>
        </div>
        <div class="order__right_subtotal-items">
          <div class="order__right_subtotal-text">Доставка</div>
          <div class="order__right_subtotal-price">{{ Math.ceil(deliveryTotal) }} <span class="rubl" > &#8399;</span></div>
        </div>
        <div class="order__right_subtotal-items">
          <div class="order__right_subtotal-text">Срок доставки</div>
          <div class="order__right_subtotal-price" v-if="shiptorOrder !== 0">{{ deliveryDays }}</div>
        </div>
      </div>
      <div class="order__right_total">
        <div class="order__right_total_items">
          <div class="order__right_total-text">Итого</div>
          <div class="order__right_total-price" v-for="item in basket.results">{{ item.price + Math.ceil(deliveryTotal) - item.total_discount  }}<span class="rubl" > &#8399;</span></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import { focus } from 'vue-focus';
  import axios from 'axios'
  import orderInfo from '../components/OrderInfo.vue'
  import orderShiptorg from '../components/OrderShiptorg.vue'
  import orderPayment from '../components/OrderPayment.vue'

  export default {
    data() {
      return {
        focusedCode: false,
        code: '',
        deliveryTotal: 0,
        deliveryDays: 0,
        promocode: ''
      }
    },
    directives: { focus: focus },
    computed: {
      basket() {
        return this.$store.state.basket.results
      },
      shiptorOrder() {
        return this.$store.state.basket.shiptor
      },
      next(){
        return this.$store.state.basket.validation
      },
    },
    components: {
      orderInfo,
      orderShiptorg,
      orderPayment
    },
    watch: {
      shiptorOrder(now){
        this.deliveryTotal = now.cost.total.sum
        this.deliveryDays = now.days
      },
      basket(now){
        if(now.results[0].cart_goods.length === 0){
          this.$router.push({name: 'basket'})
        }

        if(now.results[0].id) {
          let id = now.results[0].id;
          axios.post('/api/cart/' + id + '/check_goods/')
            .then((response) => {
              console.log(response.data[0])
              if(response.data[0] === 'false'){
                location.href = '/'
              }
            })

        }
      },
      '$route.path': 'get'
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
      checkedCode(){
        let self = this;
        const id = this.basket.results[0].id;

        axios.post('/api/cart/' + id + '/use_promocode/' + self.promocode + '/')
          .then((response) => {
            this.$store.dispatch('results');
            this.errorPopup('Промокод установлен!')
          }, (error) => {
            this.$store.dispatch('results');
            this.promocode = '';
            this.errorPopup('Не верный промокод!')
          })

      },
      backMethods(id){
        this.$store.dispatch('validation', {typeValid: 'validation', value: id})
      },
      switchItem(id, inc){
        axios.post('/api/order_goods/' + id + '/'+ inc +'/')
          .then((response) => {
            if (response.status === 200) {
              let self = this
              self.$store.dispatch('results')
            }
          })
      },
      fcCode(){
        if(this.promocode.length !== 0) {
          this.focusedCode = true
        } else {
          this.focusedCode = false
        }
      },
      get() {
        this.$store.dispatch('results')
      },
    },
    created() {
      this.get()
      this.$store.dispatch('validation', {typeValid: 'validation', value: 1})
    },
    mounted(){
    }
  }
</script>
