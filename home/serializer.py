class MenuCategoryserializer(serializer.ModelSerializer):
    class Meta:
        models=MenuCategory
        fields = ['id','name','description','price','category','is_available']

class OrderSerilaizer(serializers.ModelSerializer):
    items = MenuItemSerializer(many=True,read_only=True)
    customer = serializers.CharField(source='customer.user.username')

    class meta:
        model = Order
        fields = ['id','customer','items','total_price','created_at']