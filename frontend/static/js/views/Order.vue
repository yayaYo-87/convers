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
          <div class="order__header_list-item ">
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
        <div class="order__info_mail">
          <div class="order__info_mail-title">Информация для покупателей</div>
          <div class="order__info_input">
            <label for="email" class="order__info_input-label"
                   :class="{'order__info_input-label_active': focusedEmail}"
            >Email</label>
            <input  @focus="focusedEmail = true"
                    @blur="fcEmail()"
                    v-model="email" id="email"
                    type="email"
                    class="order__info_input-email">
          </div>
        </div>

        <div class="order__info_address">
          <div class="order__info_address-title">Адрес доставки</div>
          <div class="order__info_address-name">
            <div class="order__info_input">
              <label for="FirstName" class="order__info_input-label"
                     :class="{'order__info_input-label_active': focusedFirstName}"
              >Имя</label>
              <input  @focus="focusedFirstName = true"
                      @blur="fcFirstName()"
                      v-model="FirstName" id="FirstName"
                      type="text"
                      class="order__info_input-email">
            </div>
            <div class="order__info_input">
              <label for="LastName" class="order__info_input-label"
                     :class="{'order__info_input-label_active': focusedLastName}"
              >Фамилия</label>
              <input  @focus="focusedLastName = true"
                      @blur="fcLastName()"
                      v-model="LastName" id="LastName"
                      type="text"
                      class="order__info_input-email">
            </div>
          </div>
          <div class="order__info_address-index">
            <div class="order__info_input">
              <label for="address" class="order__info_input-label"
                     :class="{'order__info_input-label_active': focusedAddress}"
              >Адрес</label>
              <input  @focus="focusedAddress = true"
                      @blur="fcAddress()"
                      v-model="address" id="address"
                      type="text"
                      class="order__info_input-email">
            </div>
            <div class="order__info_input">
              <label for="index" class="order__info_input-label"
                     :class="{'order__info_input-label_active': focusedIndex}"
              >Индекс</label>
              <input  @focus="focusedIndex = true"
                      @blur="fcIndex()"
                      v-model="index" id="index"
                      type="text"
                      class="order__info_input-email">
            </div>
          </div>
          <div class="order__info_address-city">
            <div class="order__info_input">
              <label for="city" class="order__info_input-label"
                     :class="{'order__info_input-label_active': focusedCity}"
              >Город</label>
              <input  @focus="focusedCity = true"
                      @blur="fcCity()"
                      v-model="city" id="city"
                      type="text"
                      class="order__info_input-email">
            </div>
          </div>
          <div class="order__info_address-city">
            <div class="order__info_input">
              <label for="phone" class="order__info_input-label"
                     :class="{'order__info_input-label_active': focusedPhone}"
              >Телефон</label>
              <input  @focus="focusedPhone = true"
                      @blur="fcPhone()"
                      v-model="phone" id="phone"
                      type="tel"
                      class="order__info_input-email">
            </div>
          </div>
        </div>
        <div class="order__info_radio">
          <input id="ch1" type="checkbox">
          <label for="ch1">Сохраните эту информацию в следующий раз</label>
        </div>
        <div class="order__info_button">
          <router-link :to="{name: 'basket'}"  class="order__info_button-return">
            <svg class="order__info_button-svg" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10"><path d="M2 1l1-1 4 4 1 1-1 1-4 4-1-1 4-4"></path></svg>
            Вернуться в корзину
          </router-link>
          <div class="order__info_button-bt">
            <button>Перейти к методу доставки</button>
          </div>
        </div>
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
             v-if="basket && basket.length > 0"
             v-for="item in basket[0].cart_goods "
             >
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
          <div class="order__right_subtotal-price" v-for="item in basket">{{ item.price }}<span class="rubl" > &#8399;</span></div>
        </div>
        <div class="order__right_subtotal-items">
          <div class="order__right_subtotal-text">Доставка</div>
          <div class="order__right_subtotal-price">—</div>
        </div>
      </div>
      <div class="order__right_total">
        <div class="order__right_total_items">
          <div class="order__right_total-text">Итого</div>
          <div class="order__right_total-price" v-for="item in basket">{{ item.price }}<span class="rubl" > &#8399;</span></div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import { focus } from 'vue-focus';
  import axios from 'axios'
  export default {
    data() {
      return {
        focusedCode: false,
        code: '',

        focusedPhone: false,
        phone: '',

        focusedCity: false,
        city: '',

        email: '',
        focusedEmail: false,

        FirstName:'',
        focusedFirstName: false,

        LastName: '',
        focusedLastName: false,

        address: '',
        focusedAddress: false,

        index: '',
        focusedIndex: false
      }
    },
    directives: { focus: focus },
    computed: {
      basket() {
        return this.$store.state.basket.results.results
      }
    },
    methods: {
      fcCode(){
        if(this.code.length !== 0) {
          this.focusedCode = true
        } else {
          this.focusedCode = false
        }
      },
      fcPhone(){
        if(this.phone.length !== 0) {
          this.focusedPhone = true
        } else {
          this.focusedPhone = false
        }
      },
      fcCity(){
        if(this.city.length !== 0) {
          this.focusedCity = true
        } else {
          this.focusedCity = false
        }
      },
      fcEmail(){
        if(this.email.length !== 0) {
          this.focusedEmail = true
        } else {
          this.focusedEmail = false
        }
      },
      fcFirstName(){
        if(this.FirstName.length !== 0) {
          this.focusedFirstName = true
        } else {
          this.focusedFirstName = false
        }
      },
      fcLastName(){
        if(this.LastName.length !== 0) {
          this.focusedLastName = true
        } else {
          this.focusedLastName = false
        }
      },
      fcAddress(){
        if(this.address.length !== 0) {
          this.focusedAddress = true
        } else {
          this.focusedAddress = false
        }
      },
      fcIndex(){
        if(this.index.length !== 0) {
          this.focusedIndex = true
        } else {
          this.focusedIndex = false
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
