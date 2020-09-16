from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST) 
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)


# @login_required # GET method 요청을 처리할 수 있는 view에서만 사용
# 문제 발생
# 1. 비로그인 상태로 POST로 delete
# 2. login_required로 인해 로그인페이지로 redirect + next 파라미터 가지고
# 3. 로그인페이지에서 로그인 성공
# 4. next 파라미터 주소로 redirect됨, 이때 GET으로 처리!
@require_POST
# 5. 근데 require_POST로 405 에러 발생
# 그래서 그냥 require_POST만 이용
def delete(request, pk):
    if request.user.is_authenticated():
        article = Article.objects.get(pk=pk)
        article.delete()
    return redirect('articles:index')
