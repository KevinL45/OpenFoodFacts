"""ratatouille URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
# from django.contrib.auth.models import User
from rest_framework import routers
from ratatouille_api import views

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'ratatouille_api/menus', views.MenuViewSet)
router.register(r'ratatouille_api/products', views.ProductViewSet)
# router.register(r'products', views.ProductViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('ratatouille_api/', include('ratatouille_api.urls')),
    path('admin/', admin.site.urls),
    path('ratatouille_api/products/', views.products),
    path('ratatouille_api/search/product/<str:product_name>', views.search_product),
    path('register/', views.RegisterAPIView.as_view(),name="Register")





]
