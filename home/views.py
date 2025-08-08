from django.shortcuts import render

# Create your views here.
def homepage(request):
    restaurant = Restaurant.objects.first()
    restaurant_name = restaurant.restaurant_name if restaurant else "Restaurant"
    phone = settings.RESTAURANT_PHONE
    return render(request,'Homepage.html',{'restaurant_name':restaurant_name,'phone':phone})

def about_page(request):
    return render(request,'about.html')

def menu_list(request):
    menu_items=[
        {'name':'Paneer Butter Masala','price':180},
        {'name':'Kerala sadhya','price':100},
        {'name':'Masala dosha','price':80},
    ]
    return render(request,'menu.html',{'menu_items':menu_items})