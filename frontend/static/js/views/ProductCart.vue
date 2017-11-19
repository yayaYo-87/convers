<template>
  <div class="cart">
    <div class="cart__header">
      <router-link class="product__header-active" tag="span" :to="{ name: 'main' }" >Главная</router-link> »
      <span class="product__header-disabled">  {{result.name }}</span>
    </div>
    <div class="cart__title">
      {{result.name}}
    </div>
    <div class="cart__wrapper">
      <div class="cart__left">
        <img class="cart__left-img" :src="result.cover" alt="cover">
      </div>
      <div class="cart__right">
        <div class="cart__right_item" v-if="result.size && result.size.length !== 0 ">
          <div class="cart__right_item-name">Размер</div>
          <select>
            <option  v-for=" item in result.size"> {{ item.name }}</option>
          </select>
        </div>
        <div class="cart__right_price">
          {{ result.price }} <span class="rubl" >&#8399;</span>
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
          <div class="cart__right_item-text_h" v-if="result.title && result.title.length !== 0">
            <span>{{result.title}}</span>
          </div>
          <div class="cart__right_item-text_item" v-if="result.audience && result.audience.length !== 0">
            <div class="cart__right_item-text_item-left">Аудитория</div>
            <div class="cart__right_item-text_item-right">{{ result.audience }}</div>
          </div>
          <div class="cart__right_item-text_item" v-if="result.accessibility && result.accessibility.length !== 0">
            <div class="cart__right_item-text_item-left">Доступность</div>
            <div class="cart__right_item-text_item-right">{{ result.accessibility }}</div>
          </div>
          <div class="cart__right_item-text_item" v-if="result.easy_to_use && result.easy_to_use.length !== 0">
            <div class="cart__right_item-text_item-left">Простота использования</div>
            <div class="cart__right_item-text_item-right">{{ result.easy_to_use }}</div>
          </div>
          <div class="cart__right_item-text_item" v-if="result.author && result.author.length !== 0">
            <div class="cart__right_item-text_item-left">Автор</div>
            <div class="cart__right_item-text_item-right">{{ result.author }}</div>
          </div>
          <div class="cart__right_item-text_item" v-if="result.count_pages && result.count_pages.length !== 0">
            <div class="cart__right_item-text_item-left">Количество страниц</div>
            <div class="cart__right_item-text_item-right">{{ result.count_pages }}</div>
          </div>
          <div class="cart__right_item-text_item" v-if="result.count_pages && result.count_pages.length !== 0">
            <div class="cart__right_item-text_item-left">Формат</div>
            <div class="cart__right_item-text_item-right">{{ result.count_pages }}</div>
          </div>
          <div class="cart__right_item-text_item" v-if="result.date_publication && result.date_publication.length !== 0">
            <div class="cart__right_item-text_item-left">Дата публикации</div>
            <div class="cart__right_item-text_item-right">{{ result.date_publication }}</div>
          </div>
          <div class="cart__right_item-text_all" v-if="result.date_publication && result.date_publication.length !== 0">Общее описание</div>
          <div class="cart__right_item-text_desc" v-html="result.description"></div>
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
