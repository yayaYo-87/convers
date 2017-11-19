from django.db import models
from django.utils.safestring import mark_safe

from app.market.models import upload_to


class Slider(models.Model):
    name = models.CharField(verbose_name='Слайдер', max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Верхний слайдер'
        verbose_name_plural = 'Верхние слайдеры'


class TopSlide(models.Model):
    slider = models.ForeignKey(Slider, verbose_name='Слайдер', related_name='top_sliders')
    cover = models.ImageField(verbose_name='Обложка слайда', blank=True, upload_to=upload_to)
    link = models.URLField(verbose_name='Ссылка слайда', blank=True)
    sort_index = models.PositiveIntegerField(verbose_name='Индекс сортировки', default=0)

    def image_img(self):
        if self.cover:
            return mark_safe('<a href="{0}" target="_blank"><img src="{0}" width="200"/></a>'.format(self.cover.url))
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'
        ordering = ['sort_index']


class TopBanner(models.Model):
    cover = models.ImageField(verbose_name='Баннер', blank=True, upload_to=upload_to)
    link = models.URLField(verbose_name='Ссылка', blank=True)

    def image_img(self):
        if self.cover:
            return mark_safe('<a href="{0}" target="_blank"><img src="{0}" width="200"/></a>'.format(self.cover.url))
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True

    class Meta:
        verbose_name = 'Верхний баннер'
        verbose_name_plural = 'Верхний баннеры'


class LeftSlider(models.Model):
    name = models.CharField(verbose_name='Левый слайдер', max_length=128)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Левый слайдер'
        verbose_name_plural = 'Левые слайдеры'


class LeftSlide(models.Model):
    slider = models.ForeignKey(LeftSlider, verbose_name='Слайдер', related_name='left_sliders')
    cover = models.ImageField(verbose_name='Обложка слайда', blank=True, upload_to=upload_to)
    link = models.URLField(verbose_name='Ссылка слайда', blank=True)
    sort_index = models.PositiveIntegerField(verbose_name='Индекс сортировки', default=0)

    def image_img(self):
        if self.cover:
            return mark_safe('<a href="{0}" target="_blank"><img src="{0}" width="200"/></a>'.format(self.cover.url))
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Картинка'
    image_img.allow_tags = True

    class Meta:
        verbose_name = 'Слайд'
        verbose_name_plural = 'Слайды'
        ordering = ['sort_index']


class LeftBlog(models.Model):
    name = models.CharField(verbose_name='Название', max_length=256)
    title = models.CharField(verbose_name='Заголовок', max_length=256, blank=True)
    date = models.DateField(verbose_name='Дата', null=True, blank=True)
    description = models.CharField(verbose_name='Описание', max_length=256, null=True, blank=True)
    cover = models.ImageField(verbose_name='Обложка', blank=True, upload_to=upload_to)
    link = models.URLField(verbose_name='Ссылка', blank=True)

    def __str__(self):
        return self.name

    def image_img(self):
        if self.cover:
            return mark_safe('<a href="{0}" target="_blank"><img src="{0}" width="200"/></a>'.format(self.cover.url))
        else:
            return '(Нет изображения)'

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'