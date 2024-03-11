from rest_framework import serializers
from .models import CulturalCenter

class CulturalCenterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CulturalCenter
        fields = ['name', 'repertoire_url', 'poster_url', 'address', 'image_url']