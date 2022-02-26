from django import forms
from .models import Article
class articleForm(forms.ModelForm): # article inputa göre dinamik alan oluşturuluyor.
    class Meta:
        model = Article
        fields = ["title","content"]