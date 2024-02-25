from django import forms
from .models import CulturalCenter


class CulturalCenterForm(forms.ModelForm):
    class Meta:
        model = CulturalCenter
        fields = ['name', 'poster', 'address', 'image']

    image = forms.ImageField(required=False)