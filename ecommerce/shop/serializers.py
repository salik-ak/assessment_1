from rest_framework import serializers
from .models import Category, Product

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    price = serializers.FloatField(write_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category']

    def create(self, validated_data):
        product = Product(**validated_data)
        product.set_price(validated_data['price'])
        product.save()
        return product

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        ret['price'] = instance.get_price()
        return ret
