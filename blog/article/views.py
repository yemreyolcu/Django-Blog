from django.shortcuts import render, redirect, get_object_or_404
from .forms import articleForm
from .models import Article
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
def dashboard(request):
    articles = Article.objects.filter(author=request.user)
    context = {
        "articles":articles
    }
    return render(request,"article/dashboard.html",context)
def addarticle(request):
    form = articleForm(request.POST or None)
    if form.is_valid():
        article = form.save(commit=False)
        article.author = request.user
        article.save()
        messages.success(request,"Article has added successfully!")
        return redirect("article:dashboard")
    context = {
        "form":form
    }
    return render(request,"article/addarticle.html",context)
def detail(request,id):
    post = get_object_or_404(Article,id=id)
    context = {
        "post":post
    }
    return render(request,"article/detail.html",context)
def updateArticle(request,id):
    myarticle = get_object_or_404(Article,id=id)
    form = articleForm(request.POST or None, instance=myarticle)
    if form.is_valid():
        myarticle = form.save(commit=False)
        myarticle.author = request.user
        myarticle.save()
        messages.success(request, "Article has updated successfully!")
        return redirect("article:dashboard")
    context = {
        "form": form
    }
def deleteArticle(request):
    myarticle = get_object_or_404(Article,id=id)
    myarticle.delete()
    messages.success(request,"Article has deleted successfully!")
    return redirect("article:dashboard")