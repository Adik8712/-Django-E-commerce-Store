from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from api_main.api import CategoryViewSet, UserViewSet, ProductViewSet

router = routers.DefaultRouter()
router.register('category', CategoryViewSet, basename='category')
router.register('product', ProductViewSet, basename='product')
router.register('user', UserViewSet, basename='user')


urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('', include('api_main.urls')),
]

urlpatterns += static(settings.STATIC_URL,
            document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL,
            document_root=settings.MEDIA_ROOT)