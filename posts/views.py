from django.shortcuts import render

from .models import *


# Create your views here.
def index(request):
    posts = Post.objects.all()
    title = "Posts"
    context = {
        'posts': posts,
        'title': title
    }
    return render(request, 'index.html', context)
