from rest_framework import serializers
from .models import Category, City, Advert


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name',]
    


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['name',]
    


class AdvertSerializer(serializers.ModelSerializer):
    city = serializers.StringRelatedField()
    category = serializers.StringRelatedField()

    class Meta:
        model = Advert
        fields = ['title', 'description', 'city', 'category',]


