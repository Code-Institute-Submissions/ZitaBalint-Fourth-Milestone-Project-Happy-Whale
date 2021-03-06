from django.contrib import admin

from .models import Category, Item


class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'slug',
        'name',
        'category',
        'price',
        'review_rating',
        'image_url',
    )

    ordering = ('slug', )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'slug',
        'name',
        'image_url',
    )

    


admin.site.register(Item, ItemAdmin)
admin.site.register(Category, CategoryAdmin)
