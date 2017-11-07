<template>
  <div class="basket">
    <div class="basket__header">
      Главная » Ваша корзина
    </div>
    <h1 class="basket__title">Ваша корзина</h1>
    <div class="basket__list">
      <div class="basket__list_item basket__list_item-desc">
        Описание
      </div>
      <div class="basket__list_item">
        Цена
      </div>
      <div class="basket__list_item">
        Кол-во
      </div>
      <div class="basket__list_item">
        Удалить
      </div>
      <div class="basket__list_item">
        Итого
      </div>
    </div>
    <div class="basket__cart">
      <div class="basket__cart_item">
        <div class="basket__cart_item-img">
          <img src="../../img/cart1.jpg" alt="">
        </div>
        <div class="basket__cart_item-desc">
          <div class="basket__cart_item-desc_title">IEW Student Resource Packet</div>
          <div class="basket__cart_item-desc_text">Pairs perfectly with your IEW theme-based writing books Audience Grades 4-6; recommended as a reference for Cl...</div>
        </div>
        <div class="basket__cart_item-price">$21.00</div>
        <div class="basket__cart_item-col">
          <input type="number" value="1">
        </div>
        <div class="basket__cart_item-remove">
          <span>Удалить</span>
        </div>
        <div class="basket__cart_item-total">
          $21.00
        </div>
      </div><div class="basket__cart_item">
      <div class="basket__cart_item-img">
        <img src="../../img/cart1.jpg" alt="">
      </div>
      <div class="basket__cart_item-desc">
        <div class="basket__cart_item-desc_title">IEW Student Resource Packet</div>
        <div class="basket__cart_item-desc_text">Pairs perfectly with your IEW theme-based writing books Audience Grades 4-6; recommended as a reference for Cl...</div>
      </div>
      <div class="basket__cart_item-price">$21.00</div>
      <div class="basket__cart_item-col">
        <input type="number" value="1">
      </div>
      <div class="basket__cart_item-remove">
        <span>Удалить</span>
      </div>
      <div class="basket__cart_item-total">
        $21.00
      </div>
    </div><div class="basket__cart_item">
      <div class="basket__cart_item-img">
        <img src="../../img/cart1.jpg" alt="">
      </div>
      <div class="basket__cart_item-desc">
        <div class="basket__cart_item-desc_title">IEW Student Resource Packet</div>
        <div class="basket__cart_item-desc_text">Pairs perfectly with your IEW theme-based writing books Audience Grades 4-6; recommended as a reference for Cl...</div>
      </div>
      <div class="basket__cart_item-price">$21.00</div>
      <div class="basket__cart_item-col">
        <input type="number" value="1">
      </div>
      <div class="basket__cart_item-remove">
        <span>Удалить</span>
      </div>
      <div class="basket__cart_item-total">
        $21.00
      </div>
    </div>
    </div>
    <div class="basket__total">
      <div class="basket__total_end">
        <div class="basket__total_end-total">Итого <span>$51.99</span></div>
        <div class="basket__total_end-nal">Исключая налог и доставку</div>
      </div>
    </div>
    <div class="basket__comment">
      <div class="basket__comment_item">
        <span>Комментарий:</span>
        <textarea class="basket__comment_item-textarea" rows="3" cols="60" name="text"></textarea>
      </div>
      <div class="basket__comment_item">
        <button class="button">
          <span>Обновить</span>
        </button>
        <router-link tag="button" :to="{name: 'order'}"  class="button">
          <span>Оформление заказа</span>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
  export default {
    data() {
      return{

      }
    },
    methods: {

    }
  }
</script>
