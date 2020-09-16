from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods, require_POST
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    # articles = Article.objects.all()
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


# def new(request):
#     form = ArticleForm()
#     context = {
#         'form': form,
#     }
#     return render(request, 'articles/new.html', context)


# def create(request):
#     title = request.POST.get('title') 
#     content = request.POST.get('content')
#     article = Article(title=title, content=content)
#     article.save()
#     return redirect('articles:detail', article.pk)

@require_http_methods(['GET', 'POST'])
def create(request):
    # http method가 POST 일 때
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        # 유효성 검증
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    # GET (hjttp method가 POST가 아닌 다른 method일 때)
    else: # new
        form = ArticleForm()
    context = {
        # 1. is_valid에서 내려온 form : 에러메시지 포함
        # 2. else 구문에서 내려온 form
        'form': form,
    }
    return render(request, 'articles/create.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


@require_POST
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST': # update
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else: # edit
        # Creating a form to change an existing article.
        form = ArticleForm(instance=article)
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)


@require_http_methods(['POST'])
def delete(request, pk):
    artcile = Article.objects.get(pk=pk)
    # if request.method == 'POST':
    article.delete()
    return redirect('articles:index')
    # return redirect('articles:detail' article.pk)