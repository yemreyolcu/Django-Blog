from django.shortcuts import render, redirect, get_object_or_404,reverse
from .forms import articleForm
from .models import Article,Comment
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,"index.html")
def about(request):
    return render(request,"about.html")
@login_required(login_url="login")
def dashboard(request):
    articles = Article.objects.filter(author=request.user)
    context = {
        "articles":articles
    }
    return render(request,"article/dashboard.html",context)
@login_required(login_url="login")
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
    comments = post.comments.all()
    return render(request,"article/detail.html",{"post":post,"comments":comments})
@login_required(login_url="login")
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
    return render(request,"article/update.html",context)
@login_required(login_url="login")
def deleteArticle(request,id):
    myarticle = get_object_or_404(Article,id=id)
    myarticle.delete()
    messages.success(request,"Article has deleted successfully!")
    return redirect("article:dashboard")
def allArticle(request):
    keyword = request.GET.get("keyword")
    if keyword:
        articles = Article.objects.filter(title__contains= keyword)
        context = {
            "articles":articles
        }
        return render(request,"article/articles.html",context)
    articles = Article.objects.all()
    context = {
        "articles":articles
    }
    return render(request,"article/articles.html",context)
def addcomment(request,id):
    article = get_object_or_404(Article,id=id)
    if request.method == 'POST':
        comment_author = request.POST.get("comment_author")
        comment_content = request.POST.get("comment_content")
        newComment = Comment(comment_author=comment_author,comment_content=comment_content)
        newComment.article = article
        newComment.save()
        messages.success(request,"Comment has added!")
    return redirect(reverse("article:detail",kwargs={"id":id}))
