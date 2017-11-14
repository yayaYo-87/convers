<template>
  <div class="cart">
    <div class="cart__header">
      <router-link tag="span" :to="{ name: 'main' }" >Главная</router-link> »
      <span >  {{result.name }}</span>
    </div>
    <div class="cart__title">
      {{result.name}}
    </div>
    <div class="cart__wrapper">
      <div class="cart__left">
        <img class="cart__left-img" :src="result.cover" alt="cover">
      </div>
      <div class="cart__right">
        <div class="cart__right_item">
          <div class="cart__right_item-name">Размер</div>
          <select >
            <option  v-for=" item in result.size"> {{ item }}</option>
          </select>
        </div>
        <div class="cart__right_price">
          $9.99
        </div>
        <div class="cart__right_item cart__right_item-size">
          <div class="cart__right_item-name">Количество</div>
          <select >
            <option selected>1</option>
            <option>2</option>
            <option>3</option>
            <option>4</option>
            <option>5</option>
          </select>
        </div>
        <button class="cart__right_item-button" >
          <span>Купить</span>
        </button>
        <div class="cart__right_item-text">
          {{ result.description }}
        </div>
      </div>
    </div>
    <div class="cart__text">Вам также может понравиться</div>
    <div class="cart__rew">
      <div class="cart__item">
        <div class="cart__item-img">
          <div class="cart__item-img_wrapper">
            <img class="cart__item-img_one" src="../../img/5.png" alt="">
            <img class="cart__item-img_two" src="../../img/6.jpg" alt="">
          </div>
        </div>
        <div class="cart__item-flex">
          <div class="cart__product_item-title">
            <span>Classical Conversations 20th Anniversary Poster</span>
          </div>
          <div class="cart__item-bottom">
            <div class="cart__item-bottom_price">
              $10.00
            </div>
            <button class="cart__item-bottom_button">
              <span>Купить</span>
            </button>
          </div>
        </div>
      </div>
      <div class="cart__item">
        <div class="cart__item-img">
          <div class="cart__item-img_wrapper">
            <img class="cart__item-img_one" src="../../img/5.png" alt="">
            <img class="cart__item-img_two" src="../../img/6.jpg" alt="">
          </div>
        </div>
        <div class="cart__item-flex">
          <div class="cart__product_item-title">
            <span>Classical Conversations 20th Anniversary Poster</span>
          </div>
          <div class="cart__item-bottom">
            <div class="cart__item-bottom_price">
              $10.00
            </div>
            <button class="cart__item-bottom_button">
              <span>Купить</span>
            </button>
          </div>
        </div>
      </div>
      <div class="cart__item">
        <div class="cart__item-img">
          <div class="cart__item-img_wrapper">
            <img class="cart__item-img_one" src="../../img/5.png" alt="">
            <img class="cart__item-img_two" src="../../img/6.jpg" alt="">
          </div>
        </div>
        <div class="cart__item-flex">
          <div class="cart__product_item-title">
            <span>Classical Conversations 20th Anniversary Poster</span>
          </div>
          <div class="cart__item-bottom">
            <div class="cart__item-bottom_price">
              $10.00
            </div>
            <button class="cart__item-bottom_button">
              <span>Купить</span>
            </button>
          </div>
        </div>
      </div>
      <div class="cart__item">
        <div class="cart__item-img">
          <div class="cart__item-img_wrapper">
            <img class="cart__item-img_one" src="../../img/5.png" alt="">
            <img class="cart__item-img_two" src="../../img/6.jpg" alt="">
          </div>
        </div>
        <div class="cart__item-flex">
          <div class="cart__product_item-title">
            <span>Classical Conversations 20th Anniversary Poster</span>
          </div>
          <div class="cart__item-bottom">
            <div class="cart__item-bottom_price">
              $10.00
            </div>
            <button class="cart__item-bottom_button">
              <span>Купить</span>
            </button>
          </div>
        </div>
      </div>
    </div>
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
    methods: {
      get() {
        const self = this
        const id = this.$route.params.item
        axios.get('/api/goods/' + id + '/')
          .then(
            function (response) {
              self.result = response.data
            },
            function (error) {

            }
          )
      }
    },
    created() {
      this.get()
    }
  }
</script>
