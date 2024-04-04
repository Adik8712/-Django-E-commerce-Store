from rest_framework import routers
from .api import CategoryViewSet, UserViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register('api/category', CategoryViewSet, basename='category')
router.register('api/product', ProductViewSet, basename='product')
router.register('api/user', UserViewSet, basename='user')

urlpatterns = []

urlpatterns +=  router.urls
