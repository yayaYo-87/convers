<template>
    <div class="about">
        <div class="product__header">
            <router-link class='product__header-active' tag="span" :to="{ name: 'main' }" >Главная</router-link> »
            <span class="product__header-disabled" > Обратная связь</span>
        </div>
        <div class="about__wrapper">
            <div class="about__wrapper-left">
                <h1 class="about__title">Обратная связь</h1>
                <p>Мы очень рады видеть вас в нашем книжном интернет-магазине, который стремимся сделать удобным и функциональным. Если у вас есть предложения и пожелания, мы хотели бы их услышать! <br><br>
                Также, если у вас есть вопросы по оформлению заказов, можете воспользоваться формой ниже или отправить нам письмо на
                    <a href="mailto:info@classicalbooks.ru">info@classicalbooks.ru</a></p>
                <div class="order__shiptorg_methods-wr" v-if="loader">
                    <img class="order__shiptorg_methods-img" src="/static/img/loader.gif" alt="loader">
                </div>
                <div class="support" v-if="!loader">
                    <div class="support_input ">
                        <label for="name">Имя</label>
                        <input type="text" id="name" v-model="name">
                    </div>
                    <div class="support_input support_input-email">
                        <label for="email">E-mail</label>
                        <input type="email" id="email" v-model="email">
                    </div>
                    <div class="support_text">
                        <label for="email">Ваше сообщение</label>
                        <textarea class="support_text-area" v-model="text"></textarea>
                    </div>
                    <!--<vue-recaptcha sitekey="6LeRaD0UAAAAAEtGaHqiIVXr5_G7Od0MFWtp4i5V"-->
                    <!--ref="invisibleRecaptcha"-->
                    <!--@verify="onVerify"-->
                    <!--@expired="onExpired"-->
                    <!--&gt;</vue-recaptcha>-->
                    <button
                            @click.prevent="mailTo"
                            :disabled="!isValid"
                            class="button">
                        <span>Отправить</span>
                    </button>
                </div>
                <h3>Рекомендуемые товары</h3>
                <div class="cart__rew">
                    <div class="cart__item cart__item-width" v-for="item in limitBy(result, 3)">
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
            <div class="about__wrapper-right">
                <bar></bar>
            </div>
        </div>


    </div>
</template>

<script>
  import axios from 'axios'
  import bar from '../components/Bar.vue'
  //  import VueRecaptcha from 'vue-recaptcha';
  export default {
    data() {
      return {
        result: [],
        loader: false,
        name: '',
        email: '',
        text: '',
        emailRE: /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/
      }
    },
    components: {
      bar,
//      VueRecaptcha
    },
    computed: {
      validation: function () {
        return {
          name: !!this.name.trim(),
          text: !!this.text.trim(),
          email: this.emailRE.test(this.email),
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
      mailTo(){
        this.loader = true;
        let self = this;
        axios.post('/feedback_view/', 'name=' + self.name + '&email=' + self.email + '&text=' +self.text + '').then(
          (response) => {
            self.errorPopup('Письмо отправлено!')
            self.loader = false;
            self.name = '';
            self.email = '';
            self.text = '';
          },
          (error) => {
            self.errorPopup(error)
          }
        )
      },
      errorPopup(now){
        const newDiv = document.createElement('div')
        newDiv.classList.add('popup')
        newDiv.innerHTML = now

        document.body.appendChild(newDiv)

        setTimeout(function () {
          document.body.removeChild(newDiv)
        }, 3000)
      },
      onSubmit: function () {
        this.$refs.invisibleRecaptcha.execute()
      },
      onVerify: function (response) {
        console.log('Verify: ' + response);
      },
      onExpired: function () {
        console.log('Expired')
      },
      resetRecaptcha () {
        this.$refs.recaptcha.reset() // Direct call reset method
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
      }
    },
    created(){
      this.getRecommend()
    }

  }
</script>