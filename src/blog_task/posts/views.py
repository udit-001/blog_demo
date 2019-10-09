from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from . import models
from .forms import PostForm


def post_list(request):
    context = {
        'posts': models.Post.objects.filter(is_published=True)
    }
    return render(request, 'posts/posts_list.html', context)


def post_create(request):
    form = PostForm(request.POST or None, request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            messages.success(request, 'Post saved successfully.')
            return redirect('create')

    context = {
        'form': form,
        'title': 'Create'
    }
    return render(request, 'posts/posts_create.html', context)


def post_detail(request, slug):
    post = get_object_or_404(models.Post, slug=slug)
    context = {
        'post': post
    }
    return render(request, 'posts/posts_detail.html', context)
