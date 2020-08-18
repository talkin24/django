import requests
import random
from bs4 import BeautifulSoup
from django.shortcuts import render

# Create your views here.
def lotto(request):
    url = 'https://www.dhlottery.co.kr/common.do?method=main'
    response = requests.get(url).text
    data = BeautifulSoup(response, 'html.parser')

    selects = []
    for i in range(1,7):
        selects.append(int(data.select_one(f'#drwtNo{i}').text))

    bonus = int(data.select_one(f'#bnusNo').text)

    numbers = [n for n in range(1,46)]
    lucky = [0, 0, 0, 0, 0, 0]
    for _ in range(1000):
        check = 0
        fail = []
        result = random.choices(numbers, k=6)

        for i in range(6):
            if result[i] in selects:
                check += 1
            else:
                fail.append(result[i])
        
        if check == 6:
            lucky[0] += 1
        elif check == 5:
            if bonus in fail:
                lucky[1] += 1
            else:
                lucky[2] += 1
        elif check == 4:
            lucky[3] += 1
        elif check == 3:
            lucky[4] += 1
        else:
            lucky[5] += 1
    
    context = {
        'selects': selects,
        'bonus': bonus,
        'lucky': lucky,
    }
    return render(request, 'lotto.html', context)