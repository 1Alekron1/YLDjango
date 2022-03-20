from django.contrib import admin

from .models import Item, Tag, Category


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_published')
    list_editable = ('is_published', )
    list_display_links = ('name', )
    filter_horizontal = ('tags', )


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('slug', 'is_published')
    list_editable = ('is_published', )
    list_display_links = ('slug', )


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('slug', 'is_published')
    list_editable = ('is_published', )
    list_display_links = ('slug', )
