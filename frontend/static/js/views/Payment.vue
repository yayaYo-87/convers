<template>
    <div class="payment">
        <div class="payment__wrapper" v-if="result.Success === 'true'">
            <div class="payment__title" v-if="result.Success === 'true'">Успешный заказ!</div>
            <div class="payment__internet">Интернет-магазин "Классические беседы"</div>
            <div class="payment__item">Номер заказа: {{ result.OrderId }}</div>
            <a target="_blank" :href="'mailto:' + result.EmailReq" class="payment__mail">{{ result.EmailReq }}</a>
        </div>
        <div class="payment__wrapper" v-if="result.Success === 'false'">
            <div class="payment__title">Ошибочный заказ!</div>
            <div class="payment__internet">Интернет-магазин "Классические беседы"</div>
            <div class="payment__item">Номер заказа: {{ result.OrderId }}</div>
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
            redirect(){
                if(this.$route.query.Success === 'true') {
                    const urlSuccess = this.$route.query.OrderId.split('_')
                    if(urlSuccess[0] === 'courses') {
                        document.location.href = 'https://classicalbooks.ru/courses/#/payment?Success=' + this.$route.query.Success + '&OrderId=' + this.$route.query.OrderId + '&EmailReq=' + this.$route.query.EmailReq
                    }
                }
            }
        },
        created(){
            this.redirect()
        }
    }
</script>