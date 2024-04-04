from rest_framework import serializers
from main.models import Category, Product, Profile
from django.contrib.auth.models import User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id",'title']


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta: 
        model = Product
        fields = ["id", "image", "category", "title", "description", "price", "created_at"]



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["image", "description", "birth_data", "phone"]


class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = ['id', "username", "first_name", "last_name", "email", "profile"]
