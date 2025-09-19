class MenuCategoryserializer(serializer.ModelSerializer):
    class Meta:
        models=MenuCategory
        fields = ['id','name','description','price','category']