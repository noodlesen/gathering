from django.shortcuts import render
from django.http import HttpResponse
from gthapp.models import Author, Post
from django.shortcuts import render

from random import shuffle

# Create your views here.


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def number(request, num):
    authors = Author.objects.all()
    names = [a.nickname for a in authors]
    shuffle(names)
    names = names[:num]
    resp = ", ".join(names)
    return HttpResponse(resp)


def feed(request):
    posts = Post.objects.all()
    context = {
        "posts": posts,
        "hello": "world"
    }
    return render(request, 'gthapp/feed.html', context)
