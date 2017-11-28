import os
import uuid
from datetime import datetime

from ckeditor_uploader.fields import RichTextUploadingField
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.safestring import mark_safe
from tinymce.models import HTMLField


def upload_to(instance, filename):
    """
    Auto generate name for File and Image fields.
    :param instance: Instance of Model
    :param filename: Name of uploaded file
    :return:
    """
    name, ext = os.path.splitext(filename)
    filename = "%s%s" % (uuid.uuid4(), ext or '.jpg')
    basedir = os.path.join(instance._meta.app_label, instance._meta.model_name)
    return os.path.join(basedir, filename[:2], filename[2:4], filename)


class Catalog(models.Model):
    name = models.CharField(verbose_name='Название каталога', max_length=256)
    slug = models.SlugField(verbose_name='URL', null=True, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Каталог товара'
        verbose_name_plural = 'Каталоги товаров'

class Category(models.Model):
    catalog = models.ForeignKey('Catalog', verbose_name='Каталог', related_name='catalogs')
    name = models.CharField(verbose_name='Название категории', max_length=256)
    description = RichTextUploadingField(verbose_name='Описание категории', blank=True)
    # description = HTMLField(verbose_name='Описание категории', blank=True)
    sort_index = models.PositiveIntegerField(verbose_name='Индекс сортировки', default=0)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория товара'
        verbose_name_plural = 'Категории товаров'
        ordering = ['sort_index']


class Type(models.Model):
    name = models.CharField(verbose_name='Тип товара', max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип товара'
        verbose_name_plural = 'Типы товаров'


class Size(models.Model):
    name = models.CharField(verbose_name='Название размера', max_length=256)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Размер одежды'
        verbose_name_plural = 'Размеры одежды'


class Goods(models.Model):
    type = models.ForeignKey('Type', verbose_name='Тип', related_name='goods_types')
    category = models.ForeignKey('Category', verbose_name='Категория товаров', related_name='goods_categories', null=True)

    name = models.CharField(verbose_name='Название', max_length=256)
    price = models.PositiveIntegerField(verbose_name='Цена', blank=False)
    description = RichTextUploadingField(verbose_name='Описание', blank=True)
    # description = HTMLField(verbose_name='Описание', blank=True)
    available = models.BooleanField(verbose_name='Доcтупен сейчас', default=True)

    cover = models.ImageField(verbose_name='Выбрать фотографию обложки', blank=True, upload_to=upload_to)
    hover_cover = models.ImageField(verbose_name='Выбрать фотографию ховера обложки', blank=True, upload_to=upload_to)
    sort_index = models.PositiveIntegerField(verbose_name='Индекс сортировки', default=0)
    is_active = models.BooleanField(verbose_name='Активный', default=True)
    is_main = models.BooleanField(verbose_name='Выводить на главной', default=False)

    width = models.PositiveIntegerField(verbose_name='Ширина', default=0, null=False)
    height = models.PositiveIntegerField(verbose_name='Высота', default=0, null=False)
    length = models.PositiveIntegerField(verbose_name='Длина', default=0, null=False)
    weight = models.FloatField(verbose_name='Вес', null=False, default=0.0)

    title = models.CharField(verbose_name='Короткое описание', max_length=256, null=True, blank=True)
    audience = models.TextField(verbose_name='Аудитория', null=True, blank=True)
    accessibility = models.TextField(verbose_name='Доступность', null=True, blank=True)
    easy_to_use = models.TextField(verbose_name='Простота использования', null=True, blank=True)
    author = models.CharField(verbose_name='Автор', max_length=256, null=True, blank=True)
    count_pages = models.PositiveIntegerField(verbose_name='Количество страниц', null=True, blank=True)
    format = models.CharField(verbose_name='Формат', max_length=512, null=True, blank=True)
    date_publication = models.PositiveIntegerField(verbose_name='Дата публикации',
                                                   validators=[
                                                       MinValueValidator(2000),
                                                       MaxValueValidator(datetime.now().year)],
                                                   help_text="Введите год публикации книги <YYYY>", null=True, blank=True)

    size = models.ManyToManyField('market.Size', verbose_name='Доступные размеры', blank=True)
    related_goods = models.ManyToManyField('market.Goods', verbose_name='Похожие товары', related_name='+', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'
        ordering = ['sort_index']


class GoodsImage(models.Model):
    goods = models.ForeignKey('Goods', null=True, blank=False, verbose_name='Фото для товара', related_name='images')
    image = models.ImageField(verbose_name='Изображение', blank=False, upload_to=upload_to)
    sorting = models.PositiveIntegerField(verbose_name='Сортировка', default=0, blank=True)

    class Meta:
        verbose_name = 'Фотография товара'
        verbose_name_plural = 'Фотографии товара'
        ordering = ['sorting', ]

    def image_img(self):
        if self.image:
            return mark_safe('<a href="{0}" target="_blank"><img src="{0}" width="200"/></a>'.format(self.image.url))
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True
