<template>
    <div class="faq">
        <div class="product__header">
            <router-link class='product__header-active' tag="span" :to="{ name: 'main' }" >Главная</router-link> »
            <span class="product__header-disabled" > FAQ</span>
        </div>
        <div class="faq__wrapper">
            <h1 class="faq__title">Центр помощи</h1>
            <!--<div class="faq__search">-->
                <!--<input class="faq__search-input" type="text " placeholder="Начните вводить текст">-->
            <!--</div>-->
        </div>
        <div class="faq__items" v-for="item in resultFaq">
            <div class="faq__items_title">{{ item.name }}</div>
            <div class="faq__item" v-for="cart in item.faq_categories">
                <div class="faq__item_title">{{ cart.name }}</div>
                <item   v-for="(type, index) in cart.faq_questions"
                        :key="index"
                        :desc="type.answer"
                        :name="type.question"
                ></item>
            </div>
        </div>
        <!--<div class="faq__contacts">-->
            <!--<div class="faq__contacts-title">Не нашли то, что искали? Свяжитесь с нами.</div>-->
            <!--<button @click="popupSwitch" class="button">-->
                <!--<span>Контанк</span>-->
            <!--</button>-->
        <!--</div>-->
        <!--<div class="faq__popup" v-if="popup">-->
            <!--<div class="faq__popup_wrapper">-->
                <!--<h3 class="faq__popup_title">Контактная поддержка <div @click="popupSwitch" class="faq__popup_close"></div></h3>-->
                <!--<label class="faq__popup_label" for="email">Ваш Email</label>-->
                <!--<input id="email" class="faq__popup_mail" type="text">-->
                <!--<label class="faq__popup_label" for="text">Ваш Email</label>-->
                <!--<textarea id="text" cols="50" rows="10" class="faq__popup_text" > </textarea>-->
                <!--<div class="faq__popup_button">-->
                    <!--<button class="button">-->
                        <!--<span>Отправить</span>-->
                    <!--</button>-->
                <!--</div>-->
            <!--</div>-->
        <!--</div>-->
    </div>
</template>

<script>
  import item from '../components/FaqItem.vue'
  import axios from 'axios'

  export default {
    data() {
      return {
        resultFaq: []
      }
    },
    components: {
      item
    },
    methods:{
      getFaq(){
        const self = this
        axios.get('/api/faq_page/')
          .then(function (response) {
            self.resultFaq = response.data.results
            console.log(response.data)
          })
      }
    },
    created(){
      this.getFaq()
    }
  }
</script>