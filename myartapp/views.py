from django.shortcuts import reverse, redirect
from .forms import CulturalCenterForm
from .models import CulturalCenter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializers import CulturalCenterSerializer
from django.shortcuts import get_object_or_404


class CulturalCenterDetailAPI(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "cc_detail.html"

    def get(self, request, id=None, format=None):
        center = None
        if id is not None and id != 0:
            center = get_object_or_404(CulturalCenter, id=id)
        form = CulturalCenterForm(instance=center)
        return Response({'form': form, 'center': center})

    def post(self, request, id=None, format=None):
        action = request.POST.get('action')
        if id is not None:
            if action == 'delete':
                # Удаление существующего центра
                center = get_object_or_404(CulturalCenter, id=id)
                center.delete()
                return redirect('CulturalCenters')
            else:
                if id == 0:
                    # Добавление нового центра
                    form = CulturalCenterForm(request.POST)
                else:
                    # Обновление существующего центра
                    center = get_object_or_404(CulturalCenter, id=id)
                    form = CulturalCenterForm(request.POST, instance=center)
                if form.is_valid():
                    form.save()
                return redirect('CulturalCenterDetail', id)


class CulturalCentersAPI(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "cc.html"

    def get(self, request, format=None):
        centers = CulturalCenter.objects.all()
        context = {"centers": centers, "title": "Культурные центры"}
        return Response(context)

    def post(self, request, format=None):
        action = request.data.get('action')
        id = int(request.data.get('id'))
        if action == 'delete':
            center = get_object_or_404(CulturalCenter, id=id)
            center.delete()
        if action == 'delete_all':
            CulturalCenter.objects.all().delete()
        return redirect('CulturalCenters')
