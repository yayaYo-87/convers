<template>
    <div class="order__info-one">
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
                <div class="valid" v-show="mailV">*Не правильно указан e-mail</div>
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
                    <div class="valid" v-show="FirstNameV">*Введите имя</div>
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
                    <div class="valid" v-show="LastNameV">*Введите фамилию</div>
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
                    <div class="valid" v-show="addressV">*Введите адрес</div>
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
                    <div class="valid" v-show="indexV">*Введите индекс</div>
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
                    <div class="valid" v-show="cityV">*Введите город</div>
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
                            name="tel"
                            class="order__info_input-email">
                    <div class="valid" v-show="phoneV">*Введите корректный телефон</div>
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
    </div>
</template>

<script>
  import MaskedInput from 'vue-masked-input'

  export default {
    data() {
      return {
        phone: '',
        city: '',
        email: '',
        FirstName:'',
        LastName: '',
        address: '',
        index: '',

        emailRE: /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/,
        telRE: /^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$/,

        mailV: false,
        FirstNameV: false,
        LastNameV: false,
        addressV: false,
        indexV: false,
        cityV: false,
        phoneV: false,

        focusedPhone: false,
        focusedCity: false,
        focusedEmail: false,
        focusedFirstName: false,
        focusedLastName: false,
        focusedAddress: false,
        focusedIndex: false
      }
    },
    watch: {
      phone(now){
        if( this.validation.phone ) {
          this.$store.dispatch('validation', {typeValid: 'phone', value: now })
        }
      },
      city(now) {
        if (this.validation.city) {
          this.$store.dispatch('validation', {typeValid: 'city', value: now})
        }
      },
      email(now){
        if (this.validation.email) {
          this.$store.dispatch('validation', {typeValid: 'email', value: now})
        }
      },
      FirstName(now){
        if (this.validation.email) {
          this.$store.dispatch('validation', {typeValid: 'FirstName', value: now})
        }
      },
      LastName(now){
        if (this.validation.email) {
          this.$store.dispatch('validation', {typeValid: 'LastName', value: now})
        }
      },
      address(now){
        this.$store.dispatch('validation', {typeValid: 'address', value: now })
      },
      index(now){
        this.$store.dispatch('validation', {typeValid: 'index', value: now })
      },
    },
    computed: {
      validation: function () {
        return {
          FirstName: !!this.FirstName.trim(),
          LastName: !!this.LastName.trim(),
          city: !!this.city.trim(),
          address: !!this.address.trim(),
          index: !!this.index.trim(),
          email: this.emailRE.test(this.email),
          phone: this.telRE.test(this.phone),
        }
      },
      isValid: function () {
        let validation = this.validation;
        return Object.keys(validation).every(function (key) {
          return validation[key]
        });
      },
    },

    methods: {
      fcPhone(){
        if(this.phone.length !== 0) {
          this.focusedPhone = true
        } else {
          this.focusedPhone = false
        }
        if ( this.validation.phone === true) {
          this.phoneV = false
        }else {
          this.phoneV = true
        }
      },
      fcCity(){
        if(this.city.length !== 0) {
          this.focusedCity = true
        } else {
          this.focusedCity = false
        }
        if ( this.validation.city === true) {
          this.cityV = false
        }else {
          this.cityV = true
        }
      },
      fcEmail(){
        if(this.email.length !== 0) {
          this.focusedEmail = true
        } else {
          this.focusedEmail = false
        }
        if ( this.validation.email === true) {
          this.mailV = false
        }else {
          this.mailV = true
        }
      },
      fcFirstName(){
        if(this.FirstName.length !== 0) {
          this.focusedFirstName = true
        } else {
          this.focusedFirstName = false
        }
        if ( this.validation.FirstName === true) {
          this.FirstNameV = false
        }else {
          this.FirstNameV = true
        }
      },
      fcLastName(){
        if(this.LastName.length !== 0) {
          this.focusedLastName = true
        } else {
          this.focusedLastName = false
        }
        if ( this.validation.LastName === true) {
          this.LastNameV = false
        }else {
          this.LastNameV = true
        }
      },
      fcAddress(){
        if(this.address.length !== 0) {
          this.focusedAddress = true
        } else {
          this.focusedAddress = false
        }
        if ( this.validation.address === true) {
          this.addressV = false
        }else {
          this.addressV = true
        }
      },
      fcIndex(){
        if(this.index.length !== 0) {
          this.focusedIndex = true
        } else {
          this.focusedIndex = false
        }
        if ( this.validation.index === true) {
          this.indexV = false
        }else {
          this.indexV = true
        }
      },
    }
  }
</script>