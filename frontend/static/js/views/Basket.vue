<template>
  <div class="basket">
    <div class="basket__header">
      Главная » Ваша корзина
    </div>
    <h1 class="basket__title">Ваша корзина</h1>
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
    <div class="basket__cart" v-for="item in basket">
      <div class="basket__cart_item" v-for="cart in item.cart_goods ">
        <div class="basket__cart_item-close" @click="switchItem(cart.id, 'deactivate')"></div>
        <div class="basket__cart_item-active" v-if="!cart.active">
          <button class="button button-green" @click="switchItem(cart.id, 'activate')">
            <span>Вернуть обратно</span>
          </button>
        </div>
        <div class="basket__cart_item-img">
          <img :src="cart.goods.cover" alt="cover">
        </div>
        <div class="basket__cart_item-desc">
          <div class="basket__cart_item-desc_title">{{ cart.goods.name }}</div>
          <div class="basket__cart_item-desc_text">{{ cart.goods.description }}</div>
        </div>
        <div class="basket__cart_item-price">
          {{ cart.goods.price }}
          <span class="rubl" > &#8399;</span>
        </div>
        <div class="basket__cart_item-col">
          <input type="number" :value="cart.count">
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
        <div class="basket__total_end-nal">Исключая налог и доставку</div>
      </div>
    </div>
    <div class="basket__comment">
      <div class="basket__comment_item">
        <span>Комментарий:</span>
        <textarea class="basket__comment_item-textarea" rows="3" cols="60" name="text"></textarea>
      </div>
      <div class="basket__comment_item">
        <router-link tag="button" :to="{name: 'order'}"  class="button">
          <span>Оформление заказа</span>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
  import axios from 'axios'
  export default {
    data() {
      return{
        result: []
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
    },
    computed: {
      basket() {
        return this.$store.state.basket.results.results
      }
    },
    created(){
      this.get()
    }
  }
</script>
