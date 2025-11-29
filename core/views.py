from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from .models import Item
from .serializers import ItemSeralizer
from rest_framework import viewsets
class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSeralizer