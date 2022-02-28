from django import forms
from .models import todoForm
class todoform(forms.ModelForm): # article inputa göre dinamik alan oluşturuluyor.
    class Meta:
        model = todoForm
        fields = ["title","description","is_finished"]