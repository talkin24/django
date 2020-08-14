import random
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')


def dinner(request):
    menus = ['족발', '햄버거', '치킨', '초밥']
    pick = random.choice(menus)
    return render(request, 'dinner.html', {'pick': pick})