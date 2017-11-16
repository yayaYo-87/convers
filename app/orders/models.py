from django.db import models
from django.db.models import Sum

from app.market.models import Goods, Size


class Order(models.Model):
    STATUSES = (
        ('waiting', 'Ожидание'),
        ('processing', 'В обработке'),
        ('paid', 'Оплачено онлайн'),
        ('confirmed', 'Обработано'),
        ('cancel', 'Отменен'),
    )
    order_status = models.CharField('Статус заказа', choices=STATUSES, max_length=10, null=False, blank=False)
    city = models.CharField(max_length=255, verbose_name='Город доставки', blank=False, null=True)
    address = models.CharField(max_length=255, verbose_name='Адрес доставки', blank=False, null=True)
    index = models.CharField(max_length=255, verbose_name='Индекс доставки', blank=False, null=True)
    first_name = models.CharField(max_length=255, verbose_name='Имя', blank=False, null=True)
    last_name = models.CharField(max_length=255, verbose_name='Фамилия', blank=False, null=True)
    email = models.CharField(max_length=255, verbose_name='Email', blank=False, null=True)
    phone = models.CharField(max_length=255, verbose_name='Номер телефона', blank=False, null=True)
    total = models.PositiveIntegerField(verbose_name='Общая сумма заказа', default=0, null=True)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True, blank=True, null=True)
    total_count = models.IntegerField(verbose_name='Общее количество продуктов', blank=True, null=True, default=0)
    save_info = models.BooleanField(verbose_name='Сохранить', default=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return 'Заказ #{}'.format(self.id)

    def save(self, *args, **kwargs):
        self.total = self.get_total()
        self.total_count = self.get_total_count()
        super(Order, self).save(*args, **kwargs)

    def get_total(self):
        return float(OrderGoods.objects.filter(order=self, active=True).aggregate(sum=Sum('price'))['sum'] or 0)

    def get_total_count(self):
        return float(OrderGoods.objects.filter(order=self, active=True).aggregate(sum=Sum('count'))['sum'] or 0)


class OrderGoods(models.Model):
    order = models.ForeignKey(Order, verbose_name='Заказанные кроксы', related_name='order_goods', blank=True, null=True)
    cart = models.ForeignKey('Cart', verbose_name='Корзина', related_name='cart_goods', blank=True, null=True)
    goods = models.ForeignKey(Goods, verbose_name='Кроксы', null=True)
    size = models.ForeignKey(Size, verbose_name='Размер', null=True)
    count = models.PositiveIntegerField(verbose_name='Количество')
    price = models.FloatField(verbose_name='Цена', default=0)
    created_at = models.DateTimeField(verbose_name='Дата создания', blank=True, null=True, auto_now=False)
    active = models.BooleanField(default=True)

    def __str__(self):
        return 'Заказанный товар "{}" для заказа #{}'.format(self.goods, self.order_id)

    def save(self, *args, **kwargs):
        if not self.pk:
            super(OrderGoods, self).save(*args, **kwargs)
        self.price = self.get_price()
        super(OrderGoods, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Заказаннай товар'
        verbose_name_plural = 'Заказанные товары'
        ordering = ['id']

    def get_price(self):
        return self.price * self.count


class Cart(models.Model):
    cookie = models.CharField(verbose_name='Кука', max_length=48, blank=True, null=True)
    price = models.FloatField(verbose_name='Сумма заказа', default=0)
    total_count = models.PositiveIntegerField(verbose_name='Общее количество товаров', blank=True, null=True)

    def save(self, *args, **kwargs):
        self.price = self.get_price()
        self.total_count = self.get_total_count()
        super(Cart, self).save(*args, **kwargs)

    def get_price(self):
        return float(OrderGoods.objects.filter(cart=self, active=True).aggregate(sum=Sum('price'))['sum'] or 0)

    def get_total_count(self):
        return float(OrderGoods.objects.filter(cart=self, active=True).aggregate(sum=Sum('count'))['sum'] or 0)