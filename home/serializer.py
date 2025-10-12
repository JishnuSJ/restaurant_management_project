class MenuCategoryserializer(serializer.ModelSerializer):
    class Meta:
        models=MenuCategory
        fields = ['id','name']

class OrderSerilaizer(serializers.ModelSerializer):
    items = MenuItemSerializer(many=True,read_only=True)
    customer = serializers.CharField(source='customer.user.username')

    class meta:
        model = Order
        fields = ['id','customer','items','total_price','created_at']

class ContactFormmsubmittion(serializer.ModelSerializer):
    class Meta:
        model = ContactFormmsubmittion
        fields = ['name','email','message']


class Tableserailizer(serializer.ModelSerializer):
    class Meta:
        model =Table
        fields = ['id','table_number','capacity','is_available']

class DailyspecialSeralizer(serializer.ModelSerializer):
    class Meta:
        model=MenuItem
        fields =['id','name','decription','price']

class CreateUserReviewview(generics.CreateApiView):
    serializer_class = UserReviewSerializer
    permission_classes =[IsAuthenticatedOrReadonly]
    