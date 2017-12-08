<template>
  <div class="basket">
    <div class="basket__header">
      Главная » Ваша корзина
    </div>
    <h1 class="basket__title">Ваша корзина</h1>
    <div class="basket__recommend" v-if="basket && basket[0].cart_goods.length === 0">
      <p>Ваша корзина покупок пуста. Возможно, интересный элемент ниже представляет интерес ...</p>
      <div class="cart__rew">
        <div class="cart__item" v-for="item in limitBy(result, 3)">
          <router-link
                  tag="div"
                  :to="{ name: 'cart', params: {  item: item.id } }"
                  class="cart__item-img"
                  :class="{'cart__item-img-hover' : item.hover_cover }"
          >
            <div class="cart__item-img_wrapper">
              <img class="cart__item-img_one" :src="item.cover" alt="cover">
              <img class="cart__item-img_two" :src="item.hover_cover" alt="cover">
            </div>
          </router-link>
          <div class="cart__item-flex">
            <div class="cart__product_item-title">
              <span>{{ item.name }}</span>
            </div>
            <div class="cart__item-bottom">
              <div class="cart__item-bottom_price">
                {{ item.price }}<span class="rubl" > &#8399;</span>
              </div>
              <router-link
                      tag="button"
                      :to="{ name: 'cart', params: {  item: item.id } }"
                      class="cart__item-bottom_button">
                <span>Подробнее</span>
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="basket__wrapper" v-if="basket && basket[0].cart_goods.length > 0">
      <div class="basket__list">
        <div class="basket__list_item basket__list_item-desc">
          Описание
        </div>
        <div class="basket__list_item">
          Цена
        </div>
        <div class="basket__list_item">
          Кол-во
        </div>
        <div class="basket__list_item">
          Итого
        </div>
      </div>
      <div class="basket__cart">
        <div class="basket__cart_item" v-if="basket && basket[0].cart_goods.length > 0" v-for="cart in basket[0].cart_goods ">
          <div class="basket__cart_item-close" @click="switchItem(cart.id, 'deactivate')"></div>
          <div class="basket__cart_item-active" v-if="!cart.active">
            <button class=" button-basket" @click="switchItem(cart.id, 'activate')">
              <span>Вернуть обратно</span>
            </button>
          </div>
          <router-link
                  tag="div"
                  :to="{ name: 'cart', params: {  item: cart.goods.id } }"
                  class="basket__cart_item-img">
            <img :src="cart.goods.cover" alt="cover">
          </router-link>
          <div class="basket__cart_item-desc">
            <router-link  class="basket__cart_item-desc_title"
                          tag="div"
                          :to="{ name: 'cart', params: {  item: cart.goods.id } }"
            >{{ cart.goods.name }}</router-link>
            <div class="basket__cart_item-desc_text" v-html="cart.goods.description"></div>
          </div>
          <div class="basket__cart_item-price">
            {{ cart.goods.price }}
            <span class="rubl" > &#8399;</span>
          </div>
          <div class="basket__cart_item-col">
            <button :disabled="buttonDisabled" class="basket__cart_item-col_plus" @click="switchProductBasket(cart.id,'inc')"></button>

            <div class="basket__cart_item-col_count">{{ cart.count }}</div>
            <button class="basket__cart_item-col_minus"

                    :disabled="cart.count === 1 || buttonDisabled"
                    @click="switchProductBasket(cart.id,'dec')"></button>
          </div>
          <div class="basket__cart_item-total">
            {{ cart.price }}
            <span class="rubl" > &#8399;</span>
          </div>
        </div>
      </div>
      <div class="basket__total">
        <div class="basket__total_end">
          <div class="basket__total_end-total">Итого <span v-for="item in basket">{{ item.price }}<span class="rubl" > &#8399;</span></span></div>
        </div>
      </div>
      <div class="basket__comment" >
        <div class="basket__comment_item">
          <span>Комментарий:</span>
          <textarea class="basket__comment_item-textarea" v-model="comment" rows="3" cols="60" name="text"></textarea>
        </div>
        <div class="basket__comment_item">
          <router-link tag="button" :to="{name: 'order'}"  class="button">
            <span>Оформление заказа</span>
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import axios from 'axios'
  export default {
    data() {
      return{
        result: [],
        buttonDisabled: false,
        comment: ''
      }
    },
    watch:{
      comment(now){
        this.$store.dispatch('validation', {typeValid: 'comment', value: now})
      }
    },
    methods: {

      get() {
        this.$store.dispatch('results')
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
      getRecommend() {
        const self = this;
        axios.get('/api/main_goods/')
          .then(
            function (response) {
              self.result = response.data.results
            },
            function (error) {

            }
          )
      },
      switchProductBasket( id, inc) {
        this.buttonDisabled = true
        const self = this
        axios.post('/api/order_goods/' + id + '/'+ inc +'/', {
        })
          .then((response) => {
            if (response.status === 200) {
              self.buttonDisabled = false
              self.$store.dispatch('results')
            }
          })
      }
    },
    computed: {
      basket() {
        return this.$store.state.basket.results.results
      }
    },
    created(){
      this.get()
      this.getRecommend()
    }
  }
</script>
