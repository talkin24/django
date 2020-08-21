from django.shortcuts import render, redirect
from .models import Article

def index(request):
    # articles = Article.objects.all()[::-1]
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'index.html', context)


def new(request):
    return render(request, 'new.html')


def create(request):
    article = Article()
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:index') # index경로로 연결
    # return render(request, 'index.html') # DB에 저장되기만 하면 되니 context에 넣을 필요는 없음


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'detail.html', context)


def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'edit.html', context)


def update(request, pk):
    article = Article.objects.get(pk=pk) # create와 다른 부분
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect('articles:detail', article.pk)


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect('articles:detail', article.pk)