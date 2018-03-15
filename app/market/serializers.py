from rest_framework import serializers

from app.market.models import Catalog, Category, Goods, Type, Size, GoodsImage


class TypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Type
        fields = ['id', 'name']


class SizesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['id', 'name']


class GoodsImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsImage
        fields = ['id', 'image']


class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = [
            'id',
            'name',
            'price',
            'cover',
            'hover_cover',
        ]


class GoodsDetailSerializer(serializers.ModelSerializer):
    type = TypesSerializer()
    size = SizesSerializer(many=True, required=False)
    photos = GoodsImageSerializer(source='images', many=True)

    class Meta:
        model = Goods
        fields = [
            'id',
            'name',
            'articul',
            'type',
            'price',
            'description',
            'available',
            'cover',
            'hover_cover',
            'category',
            'is_active',
            'is_main',
            'width',
            'height',
            'length',
            'weight',
            'title',
            'audience',
            'accessibility',
            'easy_to_use',
            'author',
            'format',
            'count_pages',
            'date_publication',
            'size',
            'related_goods',
            'photos',
            'meta_title',
            'meta_description',
            'meta_keywords',
        ]


class CategorySerializer(serializers.ModelSerializer):
    goods_categories = serializers.SerializerMethodField('get_goods')

    class Meta:
        model = Category
        fields = ['id', 'name', 'goods_categories', 'description']

    def get_goods(self, obj):
        goods_queryset = Goods.objects.filter(available=True, category=obj).all()
        serializer = GoodsSerializer(instance=goods_queryset, many=True, required=False, context=self.context)

        return serializer.data


class CatalogSerializer(serializers.ModelSerializer):
    catalogs = CategorySerializer(many=True)

    class Meta:
        model = Catalog
        fields = ['id', 'name', 'slug', 'catalogs']