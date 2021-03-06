from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from tinymce.models import HTMLField


class Page(models.Model):
    name = models.CharField(verbose_name='Название страницы', null=False, max_length=256)
    slug = models.SlugField(verbose_name='URL', null=True, blank=False)
    description = RichTextUploadingField(verbose_name='Описание страницы', blank=True)
    show_top = models.BooleanField(verbose_name='Пoказывать в хэдере', default=False,)
    show_bottom = models.BooleanField(verbose_name='Пoказывать в футере', default=False,)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'


class PageFAQ(models.Model):
    name = models.CharField(verbose_name='Название страницы', null=False, max_length=256)
    slug = models.SlugField(verbose_name='URL', null=True, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQ'


class CategoryFAQ(models.Model):
    name = models.CharField(verbose_name='Название категории', null=False, max_length=256)
    page = models.ForeignKey(PageFAQ, verbose_name='Страница', related_name='faq_categories')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Название категории'
        verbose_name_plural = 'Названия категорий'


class QuestionFAQ(models.Model):
    question = models.TextField(verbose_name='Вопрос', null=False)
    answer = models.TextField(verbose_name='Ответ', null=False)
    category = models.ForeignKey(CategoryFAQ, verbose_name='Категория вопроса', related_name='faq_questions')

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'