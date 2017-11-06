from django.contrib import admin
from django.utils.safestring import mark_safe

from app.market.models import Catalog, Category, Books, Clothes, Dvd, Souvenirs


@admin.register(Catalog)
class CatalogAdmin(admin.ModelAdmin):
    model = Catalog
    fields = ['name', 'slug']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    fields = ['name', 'catalog', 'sort_index']


@admin.register(Books)
class BooksAdmin(admin.ModelAdmin):
    model = Books
    fieldsets = [
        (
            'Основные характеристики',
            {
                'classes': ('suit-tab', 'suit-tab-general',),
                'fields': (
                    'name',
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
                )
            }
        ),
        (
            'Габариты',
            {
                'classes': ('suit-tab', 'suit-tab-size',),
                'fields': (
                    'width',
                    'height',
                    'length',
                    'weight',
                )
            }
        ),
        (
            'Дополнительно',
            {
                'classes': ('suit-tab', 'suit-tab-extra',),
                'fields': (
                    'title',
                    'audience',
                    'accessibility',
                    'easy_to_use',
                    'author',
                    'count_pages',
                    'date_publication',
                )
            }
        )
    ]
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
    suit_form_tabs = (('general', 'Основные'), ('size', 'Габариты'), ('extra', 'Дополнительно'))


@admin.register(Clothes)
class ClothesAdmin(admin.ModelAdmin):
    model = Clothes
    fieldsets = [
        (
            'Основные характеристики',
            {
                'classes': ('suit-tab', 'suit-tab-general',),
                'fields': (
                    'name',
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
                )
            }
        ),
        (
            'Габариты',
            {
                'classes': ('suit-tab', 'suit-tab-size',),
                'fields': (
                    'width',
                    'height',
                    'length',
                    'weight',
                )
            }
        )
    ]
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
    suit_form_tabs = (('general', 'Основные'), ('size', 'Габариты'))


@admin.register(Dvd)
class DvdAdmin(admin.ModelAdmin):
    model = Dvd
    fieldsets = [
        (
            'Основные характеристики',
            {
                'classes': ('suit-tab', 'suit-tab-general',),
                'fields': (
                    'name',
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
                )
            }
        ),
        (
            'Габариты',
            {
                'classes': ('suit-tab', 'suit-tab-size',),
                'fields': (
                    'width',
                    'height',
                    'length',
                    'weight',
                )
            }
        )
    ]
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
    suit_form_tabs = (('general', 'Основные'), ('size', 'Габариты'))


@admin.register(Souvenirs)
class SouvenirsAdmin(admin.ModelAdmin):
    model = Souvenirs
    fieldsets = [
        (
            'Основные характеристики',
            {
                'classes': ('suit-tab', 'suit-tab-general',),
                'fields': (
                    'name',
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
                )
            }
        ),
        (
            'Габариты',
            {
                'classes': ('suit-tab', 'suit-tab-size',),
                'fields': (
                    'width',
                    'height',
                    'length',
                    'weight',
                )
            }
        )
    ]
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
    suit_form_tabs = (('general', 'Основные'), ('size', 'Габариты'))