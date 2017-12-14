<template>
    <div class="order__info-one" v-show="next === 1">
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

                <div class="order__info_input order__info_input-focus">
                    <div  class="order__info_input-label"
                          :class="{'order__info_input-label_active': focusedCity}"
                    >Город</div>
                    <input  @focus="fcCity(), focusedCity = true"
                            @blur="fcCity()"
                            v-model="city" id="city"
                            type="text"
                            autocomplete="off"
                            class="order__info_input-email ">
                    <div class="valid" v-show="cityV">*Введите город</div>
                    <div class="order__info_input-popup" v-if="resultCity.length > 0" v-show="popupCity">
                        <div class="order__info_input-popup_item"
                             :class="{ typeAheadPointer }"
                             @click="checkedCitypopup(item)"
                             v-for="item in resultCity">
                            {{ item.administrative_area }}, {{ item.short_readable }}
                        </div>
                    </div>
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
                <div class="order__info_input  order__info_input-apartment">
                    <label for="hom" class="order__info_input-label"
                           :class="{'order__info_input-label_active': focusedDom}"
                    >Дом</label>
                    <input  @focus="focusedDom = true"
                            @blur="fcDom()"
                            v-model="hom" id="hom"
                            type="text"
                            class="order__info_input-email">
                    <div class="valid" v-show="indexV">*Введите номер дома</div>
                </div>
                <div class="order__info_input">
                    <label for="apartment" class="order__info_input-label"
                           :class="{'order__info_input-label_active': focusedApartment}"
                    >Квартира</label>
                    <input  @focus="focusedApartment = true"
                            @blur="fcApartment()"
                            v-model="apartment" id="apartment"
                            type="text"
                            class="order__info_input-email">
                    <div class="valid" v-show="indexV">*Введите номер квартиры</div>
                </div>
            </div>
            <div class="order__info_address-city">
                <div class="order__info_input order__info_input-tel">
                    <label for="phone" class="order__info_input-label"
                           :class="{'order__info_input-label_active': focusedPhone}"
                    ></label>
                    <masked-input mask="\+\7(111)111-11-11" placeholder="Телефон" id="phone" type="tel"
                                  class="order__info_input-email" v-model="phone"/>
                    <div class="valid" v-show="phoneV">*Введите корректный телефон. +7 (9XX)XXX-XX-XX</div>
                </div>
            </div>
        </div>
        <div class="order__info_radio">
            <input id="ch1" type="checkbox" v-model="radio">
            <label for="ch1">Вы соглашаетесь с правилами Интернет магазина и политикой предоставления персональных данных, а также вы соглашаетесь не воспроизводить/распространять ни в какой форме никакие части изданий ООО "Классические беседы".</label>
        </div>
        <div class="order__info_button">
            <router-link :to="{name: 'basket'}"  class="order__info_button-return">
                <svg class="order__info_button-svg" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10 10"><path d="M2 1l1-1 4 4 1 1-1 1-4 4-1-1 4-4"></path></svg>
                Вернуться в корзину
            </router-link>
            <div class="order__info_button-bt">
                <button :disabled="isValid === false" @click="nextMethods()">Перейти к методу доставки</button>
            </div>
        </div>
    </div>
</template>

<script>
  import MaskedInput from 'vue-masked-input'
  import axios from 'axios'
  import vSelect  from 'vue-select'

  export default {
    data() {
      return {
        city: '',
        resultCity: [],

        radio: false,

        typeAheadPointer: 0,


        apartment: '',
        phone: '',
        email: '',
        FirstName:'',
        LastName: '',
        address: '',
        index: '',
        hom: '',
        emailRE: /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/,
        telRE: /^((\+7)[\- ]?)?(\(?(9)\d{2}\)?[\- ]?)?[\d\- ]{7,10}$/,

        mailV: false,
        FirstNameV: false,
        LastNameV: false,
        addressV: false,
        indexV: false,
        cityV: false,
        phoneV: false,
        apartmentV: false,

        focusedPhone: false,
        focusedApartment: false,
        focusedCity: false,
        focusedEmail: false,
        focusedFirstName: false,
        focusedLastName: false,
        focusedAddress: false,
        focusedIndex: false,
        focusedDom: false,

        popupCity: false,

        token: ''
      }
    },
    components:{
      vSelect,
      MaskedInput
    },
    watch: {
      validation(now){
        if(now.phone === false){
          this.phoneV = true
        }else {
          this.phoneV = false
        }
      },
      phone(now){
        if( this.validation.phone !== false ) {
          this.$store.dispatch('validation', {typeValid: 'phone', value: now })
        }
      },
      apartment(now){
        if( this.validation.apartment !== false ) {
          this.$store.dispatch('validation', {typeValid: 'apartment', value: now })
        }
      },
      city(now) {
        this.suggestSettlement()
      },
      email(now){
        if (this.validation.email !== false) {
          this.$store.dispatch('validation', {typeValid: 'email', value: now})
        }
      },
      FirstName(now){
        if (this.validation.email !== false) {
          this.$store.dispatch('validation', {typeValid: 'FirstName', value: now})
        }
      },
      LastName(now){
        if (this.validation.email !== false) {
          this.$store.dispatch('validation', {typeValid: 'LastName', value: now})
        }
      },
      address(now){
        if (this.validation.address !== false) {
          this.$store.dispatch('validation', {typeValid: 'address', value: now})
        }
      },
      hom(now){
        if (this.validation.hom !== false) {
          this.$store.dispatch('validation', {typeValid: 'hom', value: now})
        }
      },
      index(now){
        if (this.validation.index !== false) {
          this.$store.dispatch('validation', {typeValid: 'index', value: now})
        }
      },
    },
    computed: {
      next(){
        return this.$store.state.basket.validation
      },
      validation: function () {
        return {
          FirstName: !!this.FirstName.trim(),
          LastName: !!this.LastName.trim(),
          radio: !!this.radio,
          city: !!this.city.trim(),
          address: !!this.address.trim(),
          apartment: !!this.apartment.trim(),
          index: !!this.index.trim(),
          hom: !!this.hom.trim(),
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
      typeAheadUp(){

      },
      checkedCitypopup(item){
        this.city = item.administrative_area + item.short_readable
        this.$store.dispatch('validation', {typeValid: 'city', value: item})

      },
      suggestSettlement() {
        const self = this;
        const query = this.city


        axios.post('/shiptorg/', {
          json: {
            "id": "JsonRpcClient.js",
            "jsonrpc": "2.0",
            "method": "suggestSettlement",
            "params": {
              "query": query,
              "country_code": "RU"
            }
          }
        }).then(
          function (response) {
            self.resultCity = response.data.result
          }
        )
      },
      nextMethods(){
        this.$store.dispatch('validation', {typeValid: 'validation', value: 2})
      },
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
        this.popupCity = true;
        if(this.city.length !== 0) {
          this.focusedCity = true
        } else {
          this.focusedCity = false
        }

        if(this.$store.state.basket.city.length > 0){

        }else {
          this.city = ''
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
      fcDom(){
        if(this.hom.length !== 0) {
          this.focusedDom = true
        } else {
          this.focusedDom = false
        }
        if ( this.validation.hom === true) {
          this.domV = false
        }else {
          this.domV = true
        }
      },
      fcApartment(){
        if(this.apartment.length !== 0) {
          this.focusedApartment = true
        } else {
          this.focusedApartment = false
        }
        if ( this.validation.apartment === true) {
          this.apartmentV = false
        }else {
          this.apartmentV = true
        }
      }
    },
    created(){


    },
    mounted() {


    }
  }
</script>

