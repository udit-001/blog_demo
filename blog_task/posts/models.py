from django.db import models
from tinymce import HTMLField
from django.shortcuts import reverse


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, max_length=255)
    overview = models.CharField(max_length=200)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='posts'
    )
    featured_image = models.ImageField(max_length=255)
    content = HTMLField()
    seo_title = models.CharField(max_length=60, verbose_name='SEO Title')
    seo_description = models.CharField(
        max_length=160, verbose_name='SEO Description')
    created_at = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={
            'slug': self.slug
        })

    def __str__(self):
        return self.title
