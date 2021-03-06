import nested_admin
from django.contrib import admin
from import_export import resources
from import_export.admin import ExportMixin

from app.orders.models import OrderGoods, Order, Promocode


class BaseProductInline(nested_admin.NestedTabularInline):
    extra = 0
    can_delete = False

    def has_add_permission(self, request):
        return False


class OrderGoodsInline(BaseProductInline):
    model = OrderGoods
    readonly_fields = ['goods', 'count', 'price', 'created_at', 'size']
    fields = ['goods', 'count', 'price', 'created_at', 'size']


class OrderResource(resources.ModelResource):
    class Meta:
        model = Order
        fields = [
            'id',
            'total',
            'total_discount',
            'total_delivery',
            'total_count',
            'created_at',
            'order_status',
            'order_delivery',
            'city',
            'address',
            'home',
            'index',
            'first_name',
            'last_name',
            'email',
            'phone',
            'delivery_point_name',
            'administrative_area',
            'settlement',
            'apartment',
            'comment',
        ]


class OrderModelAdmin(ExportMixin, admin.ModelAdmin):
    save_as_continue = False
    save_as = False
    list_display = [
        'id',
        'phone',
        'first_name',
        'last_name',
        'order_delivery',
        'city',
        'address',
        'order_status',
        'created_at',
        'total',
        'total_delivery',
        'total_discount',
    ]
    list_filter = ['order_status', 'created_at', 'city', ]
    fields = [
        'total',
        'total_discount',
        'total_delivery',
        'total_count',
        'created_at',
        'order_status',
        'order_delivery',
        'city',
        'address',
        'home',
        'index',
        'first_name',
        'last_name',
        'email',
        'phone',
        'delivery_point_name',
        'administrative_area',
        'settlement',
        'apartment',
        'comment',

    ]
    readonly_fields = [
        'total',
        'total_discount',
        'total_delivery',
        'total_count',
        'created_at',
        'order_status',
        'order_delivery',
        'city',
        'address',
        'home',
        'index',
        'first_name',
        'last_name',
        'email',
        'phone',
        'delivery_point_name',
        'administrative_area',
        'settlement',
        'apartment',
    ]
    inlines = [OrderGoodsInline, ]
    actions = None
    resource_class = OrderResource


@admin.register(Promocode)
class PromocodeAdmin(admin.ModelAdmin):
    model = Promocode
    fields = ['code', 'discount', 'used']

admin.site.register(Order, OrderModelAdmin)
