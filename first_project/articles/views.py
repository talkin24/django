import random
from datetime import datetime
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def dinner(request):
    menus = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menus)
    context = {
        'pick': pick,
    }
    return render(request, 'dinner.html', context)


def hello(request, name):
    context = {
        'name': name,
    }
    return render(request, 'hello.html', context)


def dtl_practice(request):
    menus = ['짜장면', '탕수육', '짬뽕']
    empty_list = []
    context = {
        'menus': menus,
        'empty_list': empty_list,
    }
    return render(request, 'dtl_practice.html', context)


def throw(request):
    return render(request, 'throw.html')


def catch(request):
    # throw에서 보낸 form 데이터를 받아야 함
    # request.GET['name']
    name = request.GET.get('name')
    age = request.GET.get('age')
    context = {
        'name': name,
        'age': age,
    }
    return render(request, 'catch.html', context)


def times(request, num1, num2):
    result = num1 * num2
    context = {
        'num1': num1,
        'num2': num2,
        'result': result,
    }
    return render(request, 'times.html', context)


def HW(request):
    menus = ['hamburger', 'sushi', 'coffee']
    posts = ['starbucks', 'idiya', 'cafebene']
    users = []
    today = datetime.now()
    context = {
        "menus": menus,
        "posts": posts,
        "users": users,
        "today": today,
    }
    return render(request, 'HW.html', context)