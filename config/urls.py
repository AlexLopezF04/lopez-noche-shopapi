from django.contrib import admin # <--- 1. Importa el módulo admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from store.views.health import health_check

router = DefaultRouter()
# Aquí irán tus viewsets más adelante, ej: router.register(r'products', ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls), # <--- 2. Agrega la ruta del administrador
    path('health/', health_check),
    path('', include(router.urls)),
]