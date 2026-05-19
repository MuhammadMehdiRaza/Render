from django.shortcuts import render,redirect,get_object_or_404
from .models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .ai_helper import generate
# Create your views here.
def home(req):
    posts=Post.objects.all().order_by("-date")
    return render(req,"app/home.html",{"post":posts})

def detailPost(req):
    posts=Post.objects.all().order_by("-date")
    return render(req,"app/detailPost.html",{"post":posts})

@login_required
def create(req):
    if req.method=="POST":
        title=req.POST.get("title")
        category=req.POST.get("category")
        content=req.POST.get("content")
        Post.objects.create(
            author=req.user,
            title=title,
            category=category,
            content=content
        )    
        return redirect("home")
    return render(req,"app/createPost.html")

@login_required
def edit(req,pk):
    post=get_object_or_404(Post,pk=pk)
    if req.user!=post.author:
        return redirect("home")
    if req.method=="POST":
        post.title=req.POST.get("title")
        post.category=req.POST.get("category")
        post.content=req.POST.get("content")
        post.save()
        return redirect("home")
    return render(req,"app/createPost.html",{"post":post})

@login_required
def delete(req,pk):
    post=get_object_or_404(Post,pk=pk)
    if req.user!=post.author:
        return redirect("home")
    if req.method=="POST":
        post.delete()
        return redirect("home")
    return render(req,"app/deletePost.html",{"post":post})

def summary(req,pk):
    post=get_object_or_404(Post,pk=pk)
    summary=generate(post.content)

    return render(req,"app/ai_summary.html",{
        "post":post,
        "summary":summary
    })
    



