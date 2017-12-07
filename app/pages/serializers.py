from rest_framework import serializers

from app.pages.models import Page, PageFAQ, CategoryFAQ, QuestionFAQ


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ['id', 'name', 'slug', 'description', 'show_top', 'show_bottom']


class QuestionFAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuestionFAQ
        fields = ['id', 'question', 'answer',]


class CategoryFAQSerializer(serializers.ModelSerializer):
    faq_questions = QuestionFAQSerializer(many=True)

    class Meta:
        model = CategoryFAQ
        fields = ['id', 'name', 'faq_questions']


class PageFAQSerializer(serializers.ModelSerializer):
    faq_categories = CategoryFAQSerializer(many=True)

    class Meta:
        model = PageFAQ
        fields = ['id', 'name', 'slug', 'faq_categories']