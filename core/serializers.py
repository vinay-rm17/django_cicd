from rest_framework import serializers
from .models import Item
class ItemSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'quantity']