from ratatouille_api.models import Product
from rest_framework import serializers
from ratatouille_api.models import User

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['name']

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=128, min_length=6, write_only=True
    )

    class Meta:
        model = User
        fields = ['firstname','lastname','email','password']

    # def create (self, validated_data):
    #     return User.objects.create_user(validated_data)
