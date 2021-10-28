from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from .models import Article, Category


# Create your views here.

def home(request, page=1):
    article_list = Article.objects.published()
    paginator = Paginator(article_list , 2)
    #page = request.GET.get('page')
    page_obj = paginator.get_page(page)
    context = {
        "articles": page_obj,
    }
    return render(request, "blog/homePage.html", context)


def articleDetails(request, slug):
    context = {
        "article": get_object_or_404(Article.objects.published(), slug=slug),
    }
    return render(request,"blog/post.html", context)


def categoryPage(request, slug, page=1):
    category = get_object_or_404(Category.objects.active(), slug=slug)
    article_list = category.articles.published()
    paginator = Paginator(article_list , 2)
    page_obj = paginator.get_page(page)
    context = {
        "category" : category,
        "articles" : page_obj
    }
    return render(request, "blog/categoryPage.html", context)


def authorPage(request, username, page=1):
    author = get_object_or_404(User, username=username)
    article_list = author.articles.published()
    paginator = Paginator(article_list , 4)
    page_obj = paginator.get_page(page)
    context = {
        "author" : author,
        "articles" : page_obj
    }
    return render(request, "blog/author.html", context)