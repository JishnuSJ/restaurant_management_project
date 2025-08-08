from django.shortcuts import render

# Create your views here.
def homepage(request):
    restaurant = Restaurant.objects.first()
    restaurant_name = restaurant.restaurant_name if restaurant else "Restaurant"
    return render(request,'Homepage.html',{'restaurant_name':restaurant_name})

def about_page(request):
    return render(request,'about.html')