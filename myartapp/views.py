from django.shortcuts import reverse
from .forms import CulturalCenterForm
from .models import CulturalCenter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import CulturalCenterSerializer


class CulturalCenterDetailAPI(APIView):

    def get(self, request, id=None, format=None):
        if id is not None and id != 0:
            center = CulturalCenter.objects.get(id=id)
            serializer = CulturalCenterSerializer(center)
            return Response(serializer.data)
        else:
            return Response({'error': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, id=None, format=None):
        if id is not None:
            if id == 0:
                # Добавление нового центра
                serializer = CulturalCenterSerializer(data=request.data)
            else:
                # Обновление существующего центра
                center = CulturalCenter.objects.get(id=id)
                serializer = CulturalCenterSerializer(center, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Invalid request'}, status=status.HTTP_400_BAD_REQUEST)


class CulturalCentersAPI(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "cc.html"

    def get(self, request, format=None):
        form = CulturalCenterForm()
        centers = CulturalCenter.objects.all()
        context = {"form": form, "centers": centers, "title": "Культурные центры"}
        return Response(context)

    def post(self, request, format=None):
        action = request.data.get('action')
        if action == 'delete_all':
            CulturalCenter.objects.all().delete()
        return Response()
