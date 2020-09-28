from django.shortcuts import render, redirect, get_object_or_404
from .models import Either, Comment
from .forms import EitherForm, CommentForm
import random

def index(request):
    eithers = Either.objects.order_by('-pk')
    context = {
        'eithers': eithers,
    }
    return render(request, 'eithers/index.html', context)


def create(request):
    if request.method == 'POST':
        form = EitherForm(request.POST) 
        if form.is_valid():
            either = form.save()
            return redirect('eithers:detail', either.pk)
    else:
        form = EitherForm()
    context = {
        'form': form,
    }
    return render(request, 'eithers/create.html', context)


def detail(request, pk):
    either = get_object_or_404(Either, pk=pk)
    comment_form = CommentForm()
    comments = either.comment_set.all()
    left_num = len(Comment.objects.filter(vote='LEFT', either_id=either.pk))/len(Comment.objects.filter(either_id=either.pk))
    left_num = round(left_num, 4) * 100
    right_num = len(Comment.objects.filter(vote='RIGHT', either_id=either.pk))/len(Comment.objects.filter(either_id=either.pk))
    right_num = round(right_num, 4) * 100
    context = {
        'either': either,
        'comment_form': comment_form,
        'comments': comments,
        'left_num': left_num,
        'right_num': right_num,
    }
    return render(request, 'eithers/detail.html', context)


def comments_create(request, pk):
    either = get_object_or_404(Either, pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.either = either
        comment.save()
        return redirect('eithers:detail', either.pk)
    context = {
        'comment_form': comment_form,
        'either': either,
    }
    return render(request, 'eithers/detail.html', context)


def random(request):
    either = Either.objects.order_by('?')[0]
    context = {
        'either': either,
    }
    return redirect('eithers:detail', either.pk)