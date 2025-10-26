from django.contrib import admin

# Register your models here.
class RestaurantAdmin(admin.ModelAdmin):
    list_display=('name','address'.'phone','email','is_active')
    serach_field = ('name','address')
    list_filter = ('is_active',)
admin.site.register(Restaurant,RestaurantAdmin)