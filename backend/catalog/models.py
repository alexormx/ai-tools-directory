from django.db import models
from slugify import slugify


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimestampedModel):
    name = models.CharField(max_length=120, unique=True)
    slug = models.SlugField(max_length=140, unique=True, blank=True)
    description = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Tag(TimestampedModel):
    name = models.CharField(max_length=80, unique=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Tool(TimestampedModel):
    name = models.CharField(max_length=150, unique=True)
    slug = models.SlugField(max_length=180, unique=True, blank=True)
    url = models.URLField(blank=True)
    description = models.TextField(blank=True)
    pricing = models.CharField(max_length=50, blank=True, help_text="Ej: free, freemium, paid")
    rating = models.DecimalField(max_digits=3, decimal_places=2, null=True, blank=True)
    is_featured = models.BooleanField(default=False)
    categories = models.ManyToManyField(Category, related_name='tools', blank=True)
    tags = models.ManyToManyField(Tag, related_name='tools', blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Source(TimestampedModel):
    name = models.CharField(max_length=120)
    url = models.URLField()
    kind = models.CharField(max_length=60, help_text="rss|api|manual")

    def __str__(self):
        return self.name


class News(TimestampedModel):
    tool = models.ForeignKey(Tool, on_delete=models.SET_NULL, null=True, blank=True, related_name='news')
    title = models.CharField(max_length=300)
    url = models.URLField(unique=True)
    published_at = models.DateTimeField(null=True, blank=True)
    source = models.ForeignKey(Source, on_delete=models.SET_NULL, null=True, blank=True, related_name='news')
    summary = models.TextField(blank=True)

    def __str__(self):
        return self.title
