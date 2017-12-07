import nested_admin
from django.contrib import admin

from app.pages.models import Page, PageFAQ, CategoryFAQ, QuestionFAQ


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    model = Page
    fields = ['name', 'slug', 'description', 'show_top', 'show_bottom']


class QuestionFAQInline(nested_admin.NestedStackedInline):
    model = QuestionFAQ
    fields = ['question', 'answer']
    extra = 1


class CategoryFAQInline(nested_admin.NestedStackedInline):
    model = CategoryFAQ
    fields = ['name',]
    inlines = [QuestionFAQInline, ]
    extra = 1


@admin.register(PageFAQ)
class PageFAQAdmin(nested_admin.NestedModelAdmin):
    model = PageFAQ
    fields = ['name', 'slug']
    inlines = [CategoryFAQInline, ]