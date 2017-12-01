import nested_admin
from django.contrib import admin

from app.orders.models import OrderGoods, Order


class BaseProductInline(nested_admin.NestedTabularInline):
    extra = 0
    can_delete = False

    def has_add_permission(self, request):
        return False


class OrderGoodsInline(BaseProductInline):
    model = OrderGoods
    readonly_fields = ['goods', 'count', 'price', 'created_at', 'size']
    fields = ['goods', 'count', 'price', 'created_at', 'size']


class OrderModelAdmin(admin.ModelAdmin):
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
    ]
    list_filter = ['order_status']
    readonly_fields = [
        'total',
        'total_count',
        'total_delivery',
        'created_at',
        # 'payment_method',
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
    ]
    inlines = [OrderGoodsInline, ]
    actions = None

admin.site.register(Order, OrderModelAdmin)