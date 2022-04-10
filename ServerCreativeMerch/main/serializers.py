from json import dumps

from rest_framework import serializers
from .models import *


class CategorySerialazer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class SizeSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'


class MerchSizeNumSerialazer(serializers.ModelSerializer):
    size = SizeSerialazer()

    class Meta:
        model = MerchSizeNum
        fields = ('size', 'count')


class MerchSerialazer(serializers.ModelSerializer):
    category = CategorySerialazer()
    merch_size_num = MerchSizeNumSerialazer(many=True)

    class Meta:
        model = Merch
        fields = ['id', 'title', 'photo', 'category', 'merch_size_num', 'price']


class ProfileSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['score']


class UserSerialazer(serializers.ModelSerializer):
    profile = ProfileSerialazer()

    class Meta:
        model = User
        fields = ['id', 'username', 'profile']


class OrdersSerialazer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Orders.objects.create(**validated_data)

    class Meta:
        model = Orders
        fields = ['user', 'size_count', 'basket_coast', 'spent_score', 'created_at']
