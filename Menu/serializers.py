from rest_framework import serializers
from .models import MenuItem, Category
from decimal import Decimal

class MenuItemSerializer(serializers.ModelSerializer):
    
    stock = serializers.IntegerField(source = 'inventory')
    price_after_tax = serializers.SerializerMethodField(method_name='calculate_tax')
    category = serializers.PrimaryKeyRelatedField(
        queryset = Category.objects.all(),
        write_only = True
    )
    category_name = serializers.StringRelatedField(
        source = 'category',
        read_only = True
    )

    class Meta:
        model = MenuItem
        fields = ['title', 'price', 'price_after_tax', 'stock', 'category', 'category_name']
        
    def calculate_tax(self, product:MenuItem):
        return product.price * Decimal(1.1)
        
