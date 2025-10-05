from rest_framework import serializers
from .models import Category, Tag, Tool, Source, News


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'description']


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug']


class ToolSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Tool
        fields = ['id', 'name', 'slug', 'url', 'description', 'pricing', 'rating', 'is_featured', 'categories', 'tags', 'created_at', 'updated_at']
        read_only_fields = ['slug', 'created_at', 'updated_at']


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = ['id', 'name', 'url', 'kind']


class NewsSerializer(serializers.ModelSerializer):
    tool = serializers.SlugRelatedField(slug_field='slug', queryset=Tool.objects.all(), allow_null=True, required=False)
    source = SourceSerializer(read_only=True)

    class Meta:
        model = News
        fields = ['id', 'tool', 'title', 'url', 'published_at', 'source', 'summary', 'created_at']
        read_only_fields = ['created_at']
