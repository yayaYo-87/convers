from rest_framework import serializers

from app.market.models import Catalog, Category, Books, Clothes, Dvd, Souvenirs


class ClothesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothes
        fields = [
            'id',
            'name',
            'price',
            'cover',
            'hover_cover',
        ]


class ClothesDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothes
        fields = [
            'id',
            'name',
            'price',
            'description',
            'available',
            'cover',
            'hover_cover',
            'is_active',
            'width',
            'height',
            'length',
            'weight',
        ]


class DvdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dvd
        fields = [
            'id',
            'name',
            'price',
            'cover',
            'hover_cover',
        ]


class DvdDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dvd
        fields = [
            'id',
            'name',
            'price',
            'description',
            'available',
            'cover',
            'hover_cover',
            'is_active',
            'width',
            'height',
            'length',
            'weight',
        ]


class SouvenirsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Souvenirs
        fields = [
            'id',
            'name',
            'price',
            'cover',
            'hover_cover',
        ]


class SouvenirsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Souvenirs
        fields = [
            'id',
            'name',
            'price',
            'description',
            'available',
            'cover',
            'hover_cover',
            'is_active',
            'width',
            'height',
            'length',
            'weight',
        ]


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
            'description',
            'available',
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
    clothes_categories = ClothesSerializer(many=True, required=False)
    dvd_categories = DvdSerializer(many=True, required=False)
    souvenirs_categories = SouvenirsSerializer(many=True, required=False)
    class Meta:
        model = Category
        fields = ['id', 'name', 'books_categories', 'clothes_categories', 'dvd_categories', 'souvenirs_categories',]


class CatalogSerializer(serializers.ModelSerializer):
    catalogs = CategorySerializer(many=True)
    class Meta:
        model = Catalog
        fields = ['id', 'name', 'slug', 'catalogs']