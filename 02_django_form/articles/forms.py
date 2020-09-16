from django import forms
from .models import Article

# class ArticleForm(forms.Form):
#     REGION_A = 'seoul' # DB에 저장되는 값
#     REGION_B = 'daejeon'
#     REGIONS = [
#         (REGION_A, '서울'), #사용자에게 보여지는 값
#         (REGION_B, '대전'),
#     ]

#     title = forms.CharField(max_length=10)
#     content = forms.CharField(widget=forms.Textarea)
#     region = forms.ChoiceField(choices=REGIONS, widget=forms.RadioSelect)

class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label = '제목',
        widget = forms.TextInput(attrs={
            'class': 'my-title' 'form-control',
            'placeholder': 'Enter the title',
            'maxlength': 10,
        })
    content = forms.CharField(
        label = "내용",
        widget = forms.Textarea(attrs={
            'class': 'my-content',
            'rows': 5,
            'cols': 50,
        })
        error_messages = {
            'required': '내용 넣으세요.'
        }
    )
    )

    class Meta:
        model = Article # Article 모델
        fields = '__all__' # field 전부 사용