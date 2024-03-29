from django import forms
from .models import CulturalCenter


class CulturalCenterForm(forms.ModelForm):
    class Meta:
        model = CulturalCenter
        fields = ['name', 'repertoire_url', 'poster_url', 'address', 'image_url']