from rest_framework import serializers

from main import models


class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Catalogs
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Products
        fields = '__all__'
