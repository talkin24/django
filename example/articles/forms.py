from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }