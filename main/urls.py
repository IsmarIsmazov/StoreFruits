from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CatalogViewSet, TelegramMessageViewSet

router = DefaultRouter()

router.register(r'catalogs', CatalogViewSet, basename='catalog')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'telegram-messages', TelegramMessageViewSet, basename='message')

urlpatterns = [
    path('', include(router.urls)),
]