from dataclasses import fields
from itertools import product
from orders.models import Client,TableFood,Category,Product,FoodMenu
from rest_framework import serializers

#Serializadores Base 

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        exclude = ['status']

class TableFoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = TableFood
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ['status']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    def to_representation(self,instance):
        return { 
            "id": instance.id,
            "status": instance.status,
            "created_at": instance.created_at,
            "updated_at": instance.updated_at,
            "name_product": instance.name_product,
            "price": instance.price,
            "category": instance.category.name_category
        }
        

class FoodMenuSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = FoodMenu
        exclude = ['status']

    def to_representation(self, instance):
        representacion = super().to_representation(instance)
        representacion["client"] = instance.client.name_client
        representacion["tablefood"] = instance.tablefood.name_table_flood
        return representacion