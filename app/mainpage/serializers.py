from rest_framework import serializers

from app.mainpage.models import Slider, TopSlide, TopBanner, LeftSlide, LeftSlider, LeftBlog


class TopSlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopSlide
        fields = ['id', 'cover', 'link']


class TopSliderSerializer(serializers.ModelSerializer):
    top_sliders = TopSlideSerializer(many=True, required=False)

    class Meta:
        model = Slider
        fields = ['id', 'name', 'top_sliders']


class TopBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopBanner
        fields = ['id', 'cover']


class LeftSlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeftSlide
        fields = ['id', 'cover', 'link']


class LeftSliderSerializer(serializers.ModelSerializer):
    left_sliders = LeftSlideSerializer(many=True, required=False)

    class Meta:
        model = LeftSlider
        fields = ['id', 'name', 'left_sliders']


class LeftBlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeftBlog
        fields = ['id', 'name', 'title', 'date', 'description', 'cover', 'link']