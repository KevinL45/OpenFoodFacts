from ratatouille_api.models import Product, Menu
from rest_framework import serializers
from ratatouille_api.models import User
from django.contrib.auth.hashers import make_password



class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ['name']

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(
        max_length=128, 
        min_length=6, 
        write_only=True,
        style={'input_type': 'password', 'placeholder': 'Password'}
    )
    class Meta:
        model = User
        fields = ['firstname','lastname','email','password']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)

    # def create (self, validated_data):
    #     return User.objects.create_user(validated_data)
        # fields = ['_id', 'name', 'link', 'users', 'ingredients', 'store', 'categories']

class MenuSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Menu
        fields = ['_id', 'name', 'dishes']
