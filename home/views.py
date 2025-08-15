from django.shortcuts import render

# Create your views here.
def homepage(request):
    restaurant = Restaurant.objects.first()
    restaurant_name = restaurant.restaurant_name if restaurant else "Restaurant"
    phone = {
        'restaurant_phone':settings.RESTAURANT_PHONE
    }
    return render(request,'Homepage.html',{'restaurant_name':restaurant_name,phone})

def about_page(request):
    return render(request,'about.html')

def menu_list(request):
    menu_items=[
        {'name':'Paneer Butter Masala','price':180},
        {'name':'Kerala sadhya','price':100},
        {'name':'Masala dosha','price':80},
    ]
    return render(request,'menu.html',{'menu_items':menu_items})


class CustomerDetailsview(APIView):
    def get(self,request,customer_id):
        try:
            customer = Customer.objects.get(id=customer_id)
            serializer = CustomerSerializer(customer)
            return Response(serializer.data,status=status,HTTP_200_OK)
        except Customer.DoesNotExist:
            return Response(
                {"error":"Customer not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        except Exception as e:
            return Response(
                {"error":"An excpeted error occure","details":str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

