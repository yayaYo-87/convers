<template>
  <div class="order">
    <div class="order__left">
      <div class="order__header">

        <router-link :to="{name: 'main'}" class="">
          <h1 class="order__hidden">Classical Conversations Bookstore</h1>
          <img alt="Classical Conversations Bookstore" class="order__header_logo" src="../../img/logo.png">
        </router-link>

        <div class="order__header_list ">
          <div class="order__header_list-item order__header_list-complited">
            <router-link :to="{name: 'basket'}" class="order__header_list-link" href="https://classicalconversationsbooks.com/cart">Корзина</router-link>
            <svg class="order__svg order__svg-active" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10"><path d="M2 1l1-1 4 4 1 1-1 1-4 4-1-1 4-4"></path></svg>
          </div>
          <div class="order__header_list-item " :class="{ 'order__header_list-complited': next === 2 }">
            <a class="order__header_list-link" href="https://classicalconversationsbooks.com/cart">Информация о покупателе</a>
            <svg class="order__svg order__svg-active" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10"><path d="M2 1l1-1 4 4 1 1-1 1-4 4-1-1 4-4"></path></svg>
          </div>
          <div class="order__header_list-item order__header_list-default">
            <a class="order__header_list-link" href="https://classicalconversationsbooks.com/cart">Способ доставки</a>
            <svg class="order__svg order__svg-active" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10"><path d="M2 1l1-1 4 4 1 1-1 1-4 4-1-1 4-4"></path></svg>
          </div>
          <div class="order__header_list-item order__header_list-default">
            <a class="order__header_list-link" href="https://classicalconversationsbooks.com/cart">Способ оплаты</a>
          </div>
        </div>

      </div>


      <div class="order__info">

        <order-info

        ></order-info>

        <order-shiptorg

        ></order-shiptorg>

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
      <div class="order__right_items">
        <div class="order__right_item"
             v-if="basket.results.length > 0"
             v-for="item in basket.results[0].cart_goods "
        >
          <div class="order__right_item-close" @click="switchItem(item.id, 'deactivate')"></div>
          <div class="order__right_item-active" v-if="!item.active">
            <button class=" button-basket" @click="switchItem(item.id, 'activate')">
              <span>Вернуть обратно</span>
            </button>
          </div>
          <div class="order__right_item-img">
            <div class="order__right_item-img_wrapper">
              <img :src="item.goods.cover" alt="cover">
            </div>
            <div class="order__right_item-count">{{item.count}}</div>
          </div>
          <div class="order__right_item-name">{{ item.goods.name }}</div>
          <div class="order__right_item-price">
            {{ item.goods.price }}
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
                  v-model="code" id="code"
                  type="text"
                  class="order__info_input-email">
        </div>
        <div class="order__right_code-button">
          <button>Использовать</button>
        </div>
      </div>
      <div class="order__right_subtotal">
        <div class="order__right_subtotal-items">
          <div class="order__right_subtotal-text">Промежуточный итог</div>
          <div class="order__right_subtotal-price" v-for="item in basket.results">{{ item.price }}<span class="rubl" > &#8399;</span></div>
        </div>
        <div class="order__right_subtotal-items">
          <div class="order__right_subtotal-text">Доставка</div>
          <div class="order__right_subtotal-price">—</div>
        </div>
      </div>
      <div class="order__right_total">
        <div class="order__right_total_items">
          <div class="order__right_total-text">Итого</div>
          <div class="order__right_total-price" v-for="item in basket.results">{{ item.price }}<span class="rubl" > &#8399;</span></div>
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

  export default {
    data() {
      return {
        focusedCode: false,
        code: '',
      }
    },
    directives: { focus: focus },
    computed: {
      basket() {
        return this.$store.state.basket.results
      },
      next(){
        return this.$store.state.basket.validation
      },
    },
    components: {
      orderInfo,
      orderShiptorg
    },
    methods: {
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
        if(this.code.length !== 0) {
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
    }
  }
</script>
