from rest_framework import serializers
from .models import Products


class ProductSerializer(serializers.ModelSerializer):
    price_incl_vat = serializers.SerializerMethodField('get_price_incl_vat')
    vat = serializers.SerializerMethodField('get_vat')

    class Meta:
        model = Products
        fields = '__all__'

    def get_price_incl_vat(self, obj):
        return ((obj.vatpercentage / 100) + 1) * obj.price

    def get_vat(self, obj):
        return (obj.vatpercentage / 100) * obj.price
