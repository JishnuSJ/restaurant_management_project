from django.shortcuts import render

# Create your views here.
def homepage(request):

    restaurant = Restaurant.objects.first()
    restaurant_name = restaurant.restaurant_name if restaurant else "Restaurant"
    query = request.GET.get('q','')
    cart = request.session.get('cart',{})
    total_item = sum(cart.values())
    if query:
        menu_item = MenuItem.objects.filter(name__iconntains=query)
    else:
        menu_item = MenuItem.objects.all()
    
   
    info = RestaurantInfo.objects.first()
    context = {
        'resturant_nam': info.name if info else "Our Resturant"
        'resturant_addres':info.address if info else "address not avaliable"
        'opening_hours':info.opening_hour if info else {}
        'phone':info.phone if info else "number not "
    }
    breadcrumbs = [
        {'name':'Home','url':'/'}

    ]
    form = AuthenticationForm()
    spe = TodaySpecial.objects.filter(added_on=timezone.localdate())

    return render(request,'Homepage.html',{'restaurant_namee':restaurant_name,phone},{'restaurant_name':restaurant_nam},{'resturant_address':resturant_addres}
    ,{'menu_item':menu_item,'query':query},{"total_item":total_item},{'restaurant_phone':settings.RESTAURANT_PHONE},
    {'now':timezone.location(),}{'breadcrumbs':breadcrumbs},{form:form},{'spe':spe})


def about_page(request):
    return render(request,'about.html')

def menu_list(request):
    items = menu_items.objects.filter(avaliable = True)
    menu_items=[
        {'name':'Paneer Butter Masala','price':180,},
        {'name':'Kerala sadhya','price':100},
        {'name':'Masala dosha','price':80},
    ]
    return render(request,'menu.html',{'menu_items':menu_items},{'items':items})


def add_cart(request,item_id):
    cart = request.session.get('cart',{})
    request.session['cart']=cart
    return redirect('view_cart')




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

class MenuView(APIView):
    def get(self,request):
        menu=[
            {"name":"butter chicken","description":"tomato curry","price":120},
            {"name":"porotta chicken","description":"porotta with beef curry","price":230},
            {"name":"onam sadya","description":"kerala onam sadya","price":300}
        ]
        return Response(menu)
    
def privacy-policy(request):
    return render(request,'faq.html')

    
def contactview(request):
    info = RestaurantInfo.objects.first()
    context = {
        'rest_address' = info.address if info else "address not available"
    }
    return redirct(thankyou)

def thankyou(request):
    return render(request,'thankyou.html')