from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.db.models import Sum

from app.market.models import Goods, Size


class Order(models.Model):
    STATUSES = (
        ('waiting', 'Ожидание'),
        # ('processing', 'В обработке'),
        # ('paid', 'Оплачено онлайн'),
        ('confirmed', 'Подтвержден'),
        ('cancel', 'Отменен'),
    )
    DELIVERIES = (
        ('without', 'без доставки'),
        ('shiptor', 'shiptor'),
        ('boxberry', 'boxberry'),
        ('b2c', 'b2c'),
        ('dpd', 'dpd'),
        ('iml', 'iml'),
        ('russian-post', 'Почта России'),
        ('pickpoint', 'pickpoint'),
        ('cdek', 'cdek'),
        ('shiptor-one-day', 'shiptor-one-day'),
        ('spsr', 'spsr'),
        ('shiptor-oversize', 'shiptor-oversize'),
    )
    order_status = models.CharField('Статус заказа', choices=STATUSES, max_length=10, null=False, blank=False)
    order_delivery = models.CharField('Способ доставки', choices=DELIVERIES, max_length=16, null=True, blank=False)
    city = models.CharField(max_length=255, verbose_name='Город доставки', blank=False, null=True)
    address = models.CharField(max_length=255, verbose_name='Адрес доставки', blank=False, null=True)
    index = models.CharField(max_length=255, verbose_name='Индекс доставки', blank=False, null=True)
    first_name = models.CharField(max_length=255, verbose_name='Имя', blank=False, null=True)
    last_name = models.CharField(max_length=255, verbose_name='Фамилия', blank=False, null=True)
    email = models.CharField(max_length=255, verbose_name='Email', blank=False, null=True)
    home = models.CharField(max_length=256, verbose_name='Дом', blank=False, null=True)
    phone = models.CharField(max_length=255, verbose_name='Номер телефона', blank=False, null=True)
    total = models.PositiveIntegerField(verbose_name='Cумма заказа', default=0, null=True)
    created_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True, blank=True, null=True)
    total_count = models.IntegerField(verbose_name='Общее количество продуктов', blank=True, null=True, default=0)
    total_delivery = models.PositiveIntegerField(verbose_name='Cтоимость доставки', default=0, null=True)
    total_discount = models.PositiveIntegerField(verbose_name='Размер скидки по промокоду', default=0, null=True)

    shipping_id = models.PositiveIntegerField(verbose_name='ID способа доставки', default=0, null=False)
    kladr_id = models.CharField(verbose_name='kladr_id', max_length=256, default=0, null=False)
    delivery_point = models.CharField(verbose_name='ID пункта самовывоза', max_length=256, default=0, null=True)
    administrative_area = models.CharField(verbose_name='Область', max_length=256, null=True)
    settlement = models.CharField(verbose_name='Населенный пункт', max_length=256, null=True)
    apartment = models.CharField(verbose_name='Квартира', max_length=256, null=True)
    delivery_point_name = models.CharField(verbose_name='Пункт самовывоза', max_length=256, null=True)
    comment = models.TextField(verbose_name='Комментарий', null=True, blank=True)

    send_to_shiptor = models.BooleanField(verbose_name='Отправлен в шиптор', default=False)


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
    order = models.ForeignKey(Order, verbose_name='Заказанный товар', related_name='order_goods', blank=True, null=True)
    cart = models.ForeignKey('Cart', verbose_name='Корзина', related_name='cart_goods', blank=True, null=True)
    goods = models.ForeignKey(Goods, verbose_name='Товар', null=True)
    size = models.ForeignKey(Size, verbose_name='Размер', null=True)
    count = models.PositiveIntegerField(verbose_name='Количество')
    price = models.PositiveIntegerField(verbose_name='Цена', default=0)
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
        return self.goods.price * self.count


class Cart(models.Model):
    cookie = models.CharField(verbose_name='Кука', max_length=48, blank=True, null=True)
    price = models.PositiveIntegerField(verbose_name='Сумма заказа', default=0)
    total_count = models.PositiveIntegerField(verbose_name='Общее количество товаров', blank=True, null=True)
    total_discount = models.PositiveIntegerField(verbose_name='Размер скидки по промокоду', default=0, null=True)

    def save(self, *args, **kwargs):
        self.price = self.get_price()
        self.total_count = self.get_total_count()
        super(Cart, self).save(*args, **kwargs)

    def get_price(self):
        return float(OrderGoods.objects.filter(cart=self, active=True).aggregate(sum=Sum('price'))['sum'] or 0)

    def get_total_count(self):
        return float(OrderGoods.objects.filter(cart=self, active=True).aggregate(sum=Sum('count'))['sum'] or 0)


class Promocode(models.Model):
    code = models.CharField(verbose_name='Промокод', max_length=512, null=False)
    discount = models.PositiveIntegerField(verbose_name='Скидка по промокоду(в %)')
    used = models.BooleanField(verbose_name='Использован', default=False)

    def __str__(self):
        return 'Промокод "{}" для скидки на {}%'.format(self.code, self.discount)

    class Meta:
        verbose_name = 'Промокод'
        verbose_name_plural = 'Промокоды'



#Модели созданные для управления объектами сайта курсов
class CoursesOrdersCoursescart(models.Model):
    cookie = models.CharField(max_length=48, blank=True, null=True)
    price = models.IntegerField()
    total_count = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'courses_orders_coursescart'


class CoursesOrdersCoursesorder(models.Model):
    order_status = models.CharField(max_length=10)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    total_count = models.IntegerField(blank=True, null=True)
    extra_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = 'courses_orders_coursesorder'


class CoursesOrdersOrdertickets(models.Model):
    count = models.IntegerField()
    price = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    active = models.BooleanField()
    ids = ArrayField(models.CharField(max_length=200), blank=True)
    cart = models.ForeignKey(CoursesOrdersCoursescart, related_name='cart_goods', blank=True, null=True)
    order = models.ForeignKey(CoursesOrdersCoursesorder, related_name='order_goods', blank=True, null=True)
    tickets = models.ForeignKey('PracticumTickets', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'courses_orders_ordertickets'


class PracticumArea(models.Model):
    name = models.CharField(max_length=256)
    address = models.CharField(max_length=256)
    contacts = models.TextField()
    coordinates = models.CharField(max_length=42)

    class Meta:
        managed = False
        db_table = 'practicum_area'


class PracticumCourses(models.Model):
    name = models.CharField(max_length=256)
    slug = models.CharField(max_length=50, blank=True, null=True)
    description = models.TextField()
    area = models.ForeignKey(PracticumArea, models.DO_NOTHING, blank=True, null=True)
    date_end = models.DateTimeField(blank=True, null=True)
    date_start = models.DateTimeField(blank=True, null=True)
    email = models.CharField(max_length=200, blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)
    organizer = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=10, blank=True, null=True)
    sort_index = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'practicum_courses'


class PracticumTickets(models.Model):
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.ForeignKey('PracticumTicketscategory', models.DO_NOTHING)
    courses = models.ForeignKey(PracticumCourses, models.DO_NOTHING, blank=True, null=True)
    is_children = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'practicum_tickets'


class PracticumTicketscategory(models.Model):
    name = models.CharField(max_length=256)

    class Meta:
        managed = False
        db_table = 'practicum_ticketscategory'


class CoursesOrdersChildrentickets(models.Model):
    name = models.CharField(max_length=256)
    surname = models.CharField(max_length=256)
    gender = models.CharField(max_length=10, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    camp = models.CharField(max_length=256)
    description = models.TextField()
    order = models.ForeignKey('CoursesOrdersCoursesorder', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'courses_orders_childrentickets'


class DirectorAdmitCurator(models.Model):
    name = models.CharField(max_length=512)
    email = models.CharField(max_length=255, blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'director_admit_curator'


class DirectorAdmitBriefing(models.Model):
    name = models.CharField(max_length=512)

    class Meta:
        managed = False
        db_table = 'director_admit_briefing'


class DirectorAdmitCommunity(models.Model):
    name = models.CharField(max_length=512)

    class Meta:
        managed = False
        db_table = 'director_admit_community'


class DirectorAdmitYear(models.Model):
    name = models.CharField(max_length=512)

    class Meta:
        managed = False
        db_table = 'director_admit_year'


class DirectorAdmitDirectoradmit(models.Model):
    order_status = models.CharField(max_length=10)
    extra_id = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    inn = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    curator = models.ForeignKey(DirectorAdmitCurator, models.DO_NOTHING, blank=True, null=True,
                                related_name='admit_curator')
    passport_scan = models.CharField(max_length=100, blank=True, null=True)
    reference = models.CharField(max_length=100, blank=True, null=True)
    statement = models.CharField(max_length=100, blank=True, null=True)
    passport_data = models.TextField(blank=True, null=True)
    registration_scan = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=10)
    address = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    post_index = models.CharField(max_length=255, blank=True, null=True)
    director = models.ForeignKey(DirectorAdmitCurator, models.DO_NOTHING, blank=True, null=True,
                                 related_name='admit_director')
    federal = models.CharField(max_length=255, blank=True, null=True)
    marriage_scan = models.CharField(max_length=100, blank=True, null=True)
    patronymic = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    briefing = models.ForeignKey(DirectorAdmitBriefing, models.DO_NOTHING, blank=True, null=True)
    community = models.ForeignKey(DirectorAdmitCommunity, models.DO_NOTHING, blank=True, null=True)
    years = models.ForeignKey('DirectorAdmitYear', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'director_admit_directoradmit'


class DirectorAdmitDirectorschild(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    program = models.ForeignKey('DirectorAdmitProgram', models.DO_NOTHING, blank=True, null=True)
    is_first = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'director_admit_directorschild'


class DirectorAdmitParentsadmit(models.Model):
    order_status = models.CharField(max_length=10)
    extra_id = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    patronymic = models.CharField(max_length=255, blank=True, null=True)
    passport_data = models.TextField(blank=True, null=True)
    federal = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    post_index = models.CharField(max_length=255, blank=True, null=True)
    inn = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    passport_scan = models.CharField(max_length=100, blank=True, null=True)
    registration_scan = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    text_1 = models.TextField(blank=True, null=True)
    text_2 = models.TextField(blank=True, null=True)
    text_3 = models.TextField(blank=True, null=True)
    community = models.ForeignKey(DirectorAdmitCommunity, models.DO_NOTHING, blank=True, null=True)
    years = models.ForeignKey('DirectorAdmitYear', models.DO_NOTHING, blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'director_admit_parentsadmit'


class DirectorAdmitProgram(models.Model):
    name = models.CharField(max_length=512)

    class Meta:
        managed = False
        db_table = 'director_admit_program'


class DirectorAdmitParentletter(models.Model):
    name = models.CharField(max_length=256, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    active = models.BooleanField()
    link = models.CharField(max_length=200, blank=True, null=True)
    link_text = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'director_admit_parentletter'


class DirectorAdmitParentsadmitChildrenDirector(models.Model):
    parentsadmit = models.ForeignKey(DirectorAdmitParentsadmit, models.DO_NOTHING)
    directorschild = models.ForeignKey(DirectorAdmitDirectorschild, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'director_admit_parentsadmit_children_director'
        unique_together = (('parentsadmit', 'directorschild'),)



