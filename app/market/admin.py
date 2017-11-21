from django.contrib import admin
from django.utils.safestring import mark_safe
import nested_admin

from app.market.forms import GoodsForm
from app.market.models import Catalog, Category, Goods, Type, Size, GoodsImage


class GoodsImageInline(admin.TabularInline):
    model = GoodsImage
    fields = ['image', 'image_img', 'sorting']
    readonly_fields = ['image_img', ]
    extra = 1
    suit_classes = 'suit-tab suit-tab-general'


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    model = Catalog
    fields = ['name', 'slug']


@admin.register(Type)
class TypeAdmin(admin.ModelAdmin):
    model = Type
    fields = ['name']


@admin.register(Size)
class TypeAdmin(admin.ModelAdmin):
    model = Size
    fields = ['name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    fields = ['name', 'catalog', 'sort_index', 'description']


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    model = Goods
    form = GoodsForm
    fieldsets = [
        (
            'Основные характеристики',
            {
                'classes': ('suit-tab', 'suit-tab-general',),
                'fields': (
                    'name',
                    'type',
                    'category',
                    'price',
                    'description',
                    'available',
                    'cover',
                    'image_img',
                    'hover_cover',
                    'image_hover_img',
                    'sort_index',
                    'is_active',
                    'is_main',
                )
            }
        ),
        (
            'Габариты и рекомендованные товары',
            {
                'classes': ('suit-tab', 'suit-tab-size',),
                'fields': (
                    'width',
                    'height',
                    'length',
                    'weight',
                    'related_goods'
                )
            }
        ),
        (
            'Необходимо заполнять только для товара категории "Книги"',
            {
                'classes': ('suit-tab', 'suit-tab-extra',),
                'fields': (
                    'title',
                    'audience',
                    'accessibility',
                    'easy_to_use',
                    'author',
                    'count_pages',
                    'format',
                    'date_publication',
                )
            }
        ),
        (
            'Необходимо заполнять только для товара категории "Одежда"',
            {
                'classes': ('suit-tab', 'suit-tab-clothes',),
                'fields': (
                    'size',
                )
            }
        )
    ]
    filter_horizontal = ['size', 'related_goods',]
    inlines = [GoodsImageInline, ]
    readonly_fields = ['image_img', 'image_hover_img']

    def image_img(self, obj):
        if obj.cover:
            return mark_safe('<a href="{0}" target="_blank"><img src="{0}" width="200"/></a>'.format(obj.cover.url))
        else:
            return '(Нет изображения)'

    image_img.short_description = 'Фотография обложки'
    image_img.allow_tags = True

    def image_hover_img(self, obj):
        if obj.hover_cover:
            return mark_safe('<a href="{0}" target="_blank"><img src="{0}" width="200"/></a>'.format(obj.hover_cover.url))
        else:
            return '(Нет изображения)'

    image_hover_img.short_description = 'Фотография ховера обложки'
    image_hover_img.allow_tags = True
    suit_form_tabs = (('general', 'Основные'), ('size', 'Габариты и рекомендованные товары'), ('extra', 'Для книг'), ('clothes', 'Размеры для одежды'))
    list_filter = ['category', 'type', 'is_active', 'available', 'size']
    search_fields = ['name', 'title', 'date_publication']
