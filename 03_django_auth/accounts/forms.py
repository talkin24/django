from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model() # User를 바로 여기에 집어 넣으면 안됨, active 되어 있는 유저를 사용해야 함
        fields = ('email', 'first_name', 'last_name', ) # User 안에 뭐가 있는지 모름