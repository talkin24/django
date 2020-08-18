import random
from django.shortcuts import render

# Create your views here.
def lotto(request):
    numbers = [n for n in range(1,46)]
    result = random.choices(numbers, k=6)
    context = {
        "result": result,
    }    
    return render(request, 'lotto.html', context)


def dinner(request, 저녁메뉴, 인원수):
    context = {
        '저녁메뉴': 저녁메뉴,
        '인원수': 인원수,
    }
    return render(request, 'dinner.html', context)