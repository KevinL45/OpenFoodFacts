from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.parsers import JSONParser
from rest_framework import permissions
from django.views.decorators.csrf import csrf_exempt
import json
from ratatouille_api.models import Product, Menu
from ratatouille_api.serializers import ProductSerializer, MenuSerializer
from ratatouille_api.openFoodApi_client import OpenFoodApi
# from serializers import ProductSerializer



def index(request):
    return HttpResponse("Hello, world. You're at the ratatouille api index.")

@csrf_exempt
def products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return JsonResponse(serializer.data, safe=False)
        serializer = ProductSerializer(products, many=True)
        # openFoodApi = OpenFoodApi()
        # data = openFoodApi.findProduct('djndujd')
        # return JsonResponse(data, safe=False)
        
    if request.method == 'POST':
        data = json.loads(request.body)
        product = data['product']
        if product != None:
            # serializer = ProductSerializer(product, many=True)
            name = "test_insert"
            link = product['link']
            # users = product['']
            # ingredients
            # categories
             
            product = Product.objects.create(product)
            product.save()
           
        return JsonResponse(product, safe=False)
            # serializer = Product(snippets, many=True)
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
        
# @csrf_exempt
# def store_product(request):
    # if request.method == 'POST':
    #     product = request.POST['product']
    #     if product != None:
    #         product = Product.objects.create(json.dumps(product))
    #         result = product.save()
    #     return JsonResponse(result, safe=False)



    
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

class MenuViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]

class ProductViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [permissions.AllowAny]