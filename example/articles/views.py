from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

# Create your views here.
def create(request):
    # Q1-1
    pass

def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

