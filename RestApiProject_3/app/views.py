from django.shortcuts import render
from rest_framework import viewsets
from .serializers import DeveloperSerializer
from .models import Developer
from django.views.generic import ListView, DetailView


class QuestionApi(viewsets.ModelViewSet):
    serializer_class = DeveloperSerializer
    queryset = Developer.objects.all()


class DevList(ListView):
    model = Developer
    context_object_name = 'dev'


class DevDetail(DetailView):
    model = Developer
    context_object_name = 'dev'

    def get_queryset(self):
        return Developer.objects.all()
