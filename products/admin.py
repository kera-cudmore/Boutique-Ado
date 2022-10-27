from django.contrib import admin
from .models import Product, Category


# Register your models here.
# These classes adjust how the admin panel displays


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    # ordering - this is a tuple, even though its only 1 field
    # use - in front to reverse
    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
