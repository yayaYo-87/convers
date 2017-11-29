<template>
    <div class="payment">
        <div class="payment__wrapper" v-if="result.Success === 'true'">
            <div class="payment__title" v-if="result.Success === 'true'">Успешный заказ!</div>
            <div class="payment__internet">Интрнет-магазин "Классические беседы"</div>
            <div class="payment__item">Номер заказа: {{ result.OrderId }}</div>
            <div class="payment__item">Цена: {{ result.Amount }}</div>
            <a target="_blank" :href="'mailto:' + result.EmailReq" class="payment__mail">{{ result.EmailReq }}</a>
        </div>
        <div class="payment__wrapper" v-if="result.Success === 'false'">
            <div class="payment__title">Ошибочный заказ!</div>
            <div class="payment__internet">Интрнет-магазин "Классические беседы"</div>
            <div class="payment__item">Номер заказа: {{ result.OrderId }}</div>
            <div class="payment__item">Цена: {{ result.Amount }}</div>
            <a target="_blank" :href="'mailto:' + result.EmailReq" class="payment__mail">{{ result.EmailReq }}</a>
        </div>
    </div>
</template>

<script>
  import axios from 'axios'

  export default {
    data() {
      return {

      }
    },
    computed:{
      result(){
        return this.$route.query
      }
    },
    methods: {
      order() {
        const answer = this.result;
        const self = this;

        axios.post('/change_status/' + self.result.OrderId + '/', {
          status:  self.result.Success
        }).then(
          function (response) {

          }
        )
      }
    },
    mounted(){
      this.order()
    }
  }
</script>