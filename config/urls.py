from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from store.views.health import health_check

router = DefaultRouter()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', health_check),
    path('', include(router.urls)),
]