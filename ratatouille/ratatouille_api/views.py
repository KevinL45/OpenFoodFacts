from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt
import json
from ratatouille_api.models import Product
from ratatouille_api.serializers import ProductSerializer
# from serializers import ProductSerializer



def index(request):
    return HttpResponse("Hello, world. You're at the ratatouille api index.")

@csrf_exempt
def products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)

    if request.method == 'POST':
        product_to_create = Product.objects.create(name= "test")
        product_to_create.save()
        # serializer = Product(snippets, many=True)
        return JsonResponse("OK", safe=False)
    # elif request.method == 'POST':
    #     data = JSONParser().parse(request)
    #     serializer = SnippetSerializer(data=data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return JsonResponse(serializer.data, status=201)
    #     return JsonResponse(serializer.errors, status=400)
# class ProductViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
#     # permission_classes = [permissions.IsAuthenticated]
#     permission_classes = [permissions.AllowAny]
    
