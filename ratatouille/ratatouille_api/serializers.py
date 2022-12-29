from ratatouille_api.models import Product, Menu
from rest_framework import serializers

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['_id', 'name', 'link', 'users', 'ingredients', 'store', 'categories']

class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        fields = ['_id', 'name', 'dishes']