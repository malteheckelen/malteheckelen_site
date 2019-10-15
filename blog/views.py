from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from django.template import Template
from .models import Post

def index(request):
    posts = Post.objects.filter(published=True).order_by('-published_date')
    return(render(request, 'blog/index.html', {'posts': posts}))

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.template = Template(post.text)
    return(render(request, 'blog/detail.html', {'post': post}))
