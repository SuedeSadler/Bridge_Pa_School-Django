from django.shortcuts import render

# Create your views here.
post = [
    {
        
    }
]
def home(request):
    return render(request, 'news/home.html')

def about(request):
    return render(request, 'news/about.html')