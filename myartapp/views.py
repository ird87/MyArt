from django.shortcuts import reverse
from .forms import CulturalCenterForm
from .models import CulturalCenter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer


class CulturalCenterAPI(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "cc.html"

    def get(self, request, format=None):
        form = CulturalCenterForm()
        centers = CulturalCenter.objects.all()
        context = {"form": form, "centers": centers, "title": "Культурные центры"}
        return Response(context)

    def post(self, request, format=None):
        action = request.data.get('action')
        id = request.data.get('id')
        if action == 'add':
            form = CulturalCenterForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
        elif action == 'edit':
            instance = CulturalCenter.objects.get(id=id)
            form = CulturalCenterForm(request.POST, request.FILES, instance=instance)
            if form.is_valid():
                form.save()
        elif action == 'delete':
            instance = CulturalCenter.objects.get(id=id)
            instance.delete()
        elif action == 'delete_all':
            CulturalCenter.objects.all().delete()
        elif action == 'save_all':
            for center in CulturalCenter.objects.all():
                form = CulturalCenterForm(request.POST, request.FILES, instance=center)
                if form.is_valid():
                    form.save()
        return Response()
