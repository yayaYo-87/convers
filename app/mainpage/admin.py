from django.contrib import admin

from app.mainpage.models import TopSlide, Slider, LeftSlide, LeftSlider, TopBanner, LeftBlog


class TopSlideInline(admin.StackedInline):
    model = TopSlide
    fields = ['sort_index', 'cover', 'image_img', 'link']
    readonly_fields = ['image_img',]
    extra = 1


@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    model = Slider
    fields = ['name',]
    inlines = [TopSlideInline, ]


@admin.register(TopBanner)
class TopBannerAdmin(admin.ModelAdmin):
    model = TopBanner
    fields = ['cover', 'image_img', 'link']
    readonly_fields = ['image_img',]


class LeftSlideInline(admin.StackedInline):
    model = LeftSlide
    fields = ['sort_index', 'cover', 'image_img', 'link']
    readonly_fields = ['image_img',]
    extra = 1


@admin.register(LeftSlider)
class LeftSliderAdmin(admin.ModelAdmin):
    model = LeftSlider
    fields = ['name',]
    inlines = [LeftSlideInline, ]


@admin.register(LeftBlog)
class LeftBlogAdmin(admin.ModelAdmin):
    model = LeftBlog
    fields = ['name', 'title', 'date', 'description', 'cover', 'link', 'pages']
