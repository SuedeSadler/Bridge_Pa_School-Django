from multiprocessing import context
from django.shortcuts import render
from .models import Post


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'news/home.html', context)

def about(request):
    return render(request, 'news/about.html', {'title': 'About'})