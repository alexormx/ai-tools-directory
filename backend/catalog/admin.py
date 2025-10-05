from django.contrib import admin
from .models import Category, Tag, Tool, Source, News

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at')
    search_fields = ('name',)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at')
    search_fields = ('name',)


@admin.register(Tool)
class ToolAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'pricing', 'is_featured', 'created_at')
    list_filter = ('is_featured', 'pricing')
    search_fields = ('name', 'description')
    filter_horizontal = ('categories', 'tags')


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = ('name', 'kind', 'url', 'created_at')
    search_fields = ('name', 'kind')


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'tool', 'published_at', 'url')
    search_fields = ('title', 'tool__name')
    list_filter = ('published_at',)
