<template>
    <div class="cart__item" v-if="result.available !== false">
        <router-link
                tag="div"
                :to="{ name: 'cart', params: {  item: id } }"
                class="cart__item-img">
            <div class="cart__item-img_wrapper">
                <img class="cart__item-img_one" :src="result.cover" alt="cover">
                <img class="cart__item-img_two" :src="result.hover_cover" alt="cover">
            </div>
        </router-link>
        <div class="cart__item-flex">
            <div class="cart__product_item-title">
                <span>{{ result.name }}</span>
            </div>
            <div class="cart__item-bottom">
                <div class="cart__item-bottom_price">
                    {{ result.price }}<span class="rubl" > &#8399;</span>
                </div>
                <router-link
                        tag="button"
                        :to="{ name: 'cart', params: {  item: id } }"
                        class="cart__item-bottom_button">
                    <span>Подробнее</span>
                </router-link>
            </div>
        </div>
    </div>
</template>

<script>
    import axios from 'axios'

    export default {
        props: ['id'],
        data() {
            return {
                result: []
            }
        },
        methods: {
            get() {
                const self = this;
                axios.get('/api/goods/' + this.id + '/')
                    .then(
                        function (response) {

                            self.result = response.data
                        },
                        function (error) {

                        }
                    )
            },
        },
        created() {
            this.get()
        }
    }
</script>