class MenuCategoryserializer(serializer.ModelSerializer):
    class Meta:
        models=MenuCategory
        fields = ['name']