from django import forms
from . import models
from tinymce.widgets import TinyMCE


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = models.Post
        fields = ['title', 'slug', 'overview',
                  'category', 'featured_image', 'content', 'seo_title', 'seo_description', 'is_published']
