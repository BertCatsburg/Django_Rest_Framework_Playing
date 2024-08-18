from rest_framework import serializers
from base.models import Item


class ItemSerializer(serializers.ModelSerializer):
    name_official = serializers.SerializerMethodField('get_name_official')

    class Meta:
        model = Item
        fields = '__all__'

    def get_name_official(self, obj):
        return f"Mr. {obj.name}"
