from django.contrib import admin
from .models import MenuItem, Table, Order


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'available')
    list_filter = ('category', 'available')
    search_fields = ('name', 'category')


@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('number', 'seats', 'status')
    list_filter = ('status',)
    search_fields = ('number',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'table', 'created_by', 'total_price', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('table__number', 'items__name', 'created_by__username')
    filter_horizontal = ('items',)  # makes ManyToMany items easier to select
