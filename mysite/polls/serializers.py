from rest_framework import serializers
from .models import *
class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        # model=Language
        fields=('lang','id')
class BookSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    author=serializers.CharField(max_length=100)
    title=serializers.CharField(max_length=100)
    # def create(self,validated_data):
    #     return Language.objects.create(**validated_data)
    # def update(self,instance,validated_data):
    #     pass
