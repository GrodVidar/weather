from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from .models import HeatIndex
from .serializers import HeatIndexSerializer


class HeatIndexViewSet(viewsets.ModelViewSet):
    queryset = HeatIndex.objects.all().order_by('-date')
    serializer_class = HeatIndexSerializer
