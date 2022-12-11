from multiprocessing import context
from django.shortcuts import render

# Create your views here.
posts = [
    {
        'Author': 'Suede',
        'title': 'News Post 1',
        'content': ' First news post content',
        'date_posted': 'August 29, 2022 '
    },
    {
        'Author': 'Philli',
        'title': 'News Post 2',
        'content': ' Second news post content',
        'date_posted': 'August 25, 2022 '
    }
]
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'news/home.html', context)

def about(request):
    return render(request, 'news/about.html', {'title': 'About'})