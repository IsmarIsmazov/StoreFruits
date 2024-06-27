from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

from core.utils import send_telegram_message
from .serilalizers import CatalogSerializer, ProductSerializer

from main.models import Catalogs, Products



class CatalogViewSet(ModelViewSet):
    queryset = Catalogs.objects.all()
    serializer_class = CatalogSerializer


class ProductViewSet(ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = self.queryset
        name_param = self.request.query_params.get('name', None)
        if name_param:
            queryset = queryset.filter(catalog__name__icontains=name_param)
        return queryset


class TelegramMessageViewSet(viewsets.ViewSet):

    @action(detail=False, methods=['post'])
    def send_message(self, request):
        message = request.data.get('message')
        if message:
            send_telegram_message(message)
            return Response({'status': 'Message sent'})
        else:
            return Response({'error': 'Message parameter is required'}, status=400)
