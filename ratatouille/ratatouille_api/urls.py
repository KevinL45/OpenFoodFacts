from rest_framework import routers
from .api import UserViewSet

router = routers.DefaultRouter()
router.register('register', UserViewSet, 'users')

urlpatterns = router.urls