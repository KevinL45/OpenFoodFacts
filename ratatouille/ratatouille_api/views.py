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
from ratatouille_api.openFoodApi_client import OpenFoodApi
# from serializers import ProductSerializer
from rest_framework.generics import GenericAPIView
from ratatouille_api.serializers import UserSerializer
from rest_framework import response, status
from ratatouille_api.models import User



def index(request):
    return HttpResponse("Hello, world. You're at the ratatouille api index.")

@csrf_exempt
def products(request):
    if request.method == 'GET':
        # products = Product.objects.all()
        # serializer = ProductSerializer(products, many=True)
        # return JsonResponse(serializer.data, safe=False)
        # serializer = ProductSerializer(products, many=True)
        openFoodApi = OpenFoodApi()
        data = openFoodApi.findProduct('djndujd')
        return JsonResponse(data, safe=False)
        
    if request.method == 'POST':
        product_to_create = Product.objects.create(request.body())
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


@csrf_exempt
def search_product(request, product_name):
    if request.method == 'GET':
        openFoodApi = OpenFoodApi()
        data = openFoodApi.findProduct(product_name)
        return JsonResponse(data, safe=False)
        
    


    
# def substitutes(request):
#      if request.method == 'GET':
#         # products = Product.objects.all()
#         # serializer = ProductSerializer(products, many=True)
#         # return JsonResponse(serializer.data, safe=False)
#         # serializer = ProductSerializer(products, many=True)
#         openFoodApi = OpenFoodApi()
#         data = openFoodApi.findSubtitute()
#         return JsonResponse(data, safe=False)
        
#     if request.method == 'POST':
#         product_to_create = Product.objects.create(name= "test")
#         product_to_create.save()
#         # serializer = Product(snippets, many=True)
#         return JsonResponse("OK", safe=False)

class RegisterAPIView(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]

    def post(self,request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

# def register(request):
#     user_to_create = User.objects.create(request.body())
#     user_to_create.save()
#     return JsonResponse("OK", safe=False)


    




