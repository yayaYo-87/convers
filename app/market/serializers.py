from rest_framework import serializers

from app.market.models import Catalog, Category, Books


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = [
            'id',
            'name',
            'price',
            'cover',
            'hover_cover',
        ]


class BooksDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = [
            'id',
            'name',
            'price',
            'cover',
            'hover_cover',
            'is_active',
            'width',
            'height',
            'length',
            'weight',
            'title',
            'audience',
            'accessibility',
            'easy_to_use',
            'author',
            'count_pages',
            'date_publication',
        ]


class CategorySerializer(serializers.ModelSerializer):
    books_categories = BooksSerializer(many=True, required=False)
    class Meta:
        model = Category
        fields = ['id', 'name', 'books_categories']


class CatalogSerializer(serializers.ModelSerializer):
    catalogs = CategorySerializer(many=True)
    class Meta:
        model = Catalog
        fields = ['id', 'name', 'slug', 'catalogs']