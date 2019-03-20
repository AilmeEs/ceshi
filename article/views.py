from django.shortcuts import render
from .models import Post
# Create your views here.


def delete_(request,id):
    post=Post.objects.get(id=id)
    post.delete()
    return request('/')

def index(request):
    posts=Post.objects.all()
    return render(request,'index.html',{'posts':posts})
