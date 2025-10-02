from django.db import models

class UserProfile(models.Model):
    user = models.OnetoOneField(USer,on_delete=models.CASCADE,related_name='profile')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    
    def __str__(self):
        return f"{self.name}({self.user.username})"



        

class Menu(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=6,decimal_places=2)

    def __str__(self):
        return self.name
    
    ORDER_STATUS_CHOICES = [
        ('PENDING','Pending'),
        ('CONFIRMED','Confirmed'),
        ('DELIVERED','Delivered'),
        ('CANCELLED','Cancelled'),
        
    ]

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    items = models.ManytoManyField(Menu)
    total_amount = models.DecimalField(max_digits=8,decimal_places=2)
    #status = models.CharField(max_length=10,choice=ORDER_STATUS_CHOICES,default="PENDING")
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Order by {self.customer_name} on {self.created_at.strftime('%y-%m-%d')}"



class Contactform(models.Model):
    name = models.CharField(max_digits=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)


class Menuitem(models.Model):
    name =  models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6)
    image = models.ImageField(upload_to='menu_image/',blank=True,null=True)
    available = models.BooleanField(default=True)
    category = models.ForeignKey(MenuCategory,on_delete=models.CASCADE,related_name="items")


class Restaurantinfo(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=20)
    opening_hours = models.JSONField(default=dict)
    phone = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='res_logo',blank=True,null= True)
    opening_hours = models.CharField(max_length=50,help_task="comma separated days like 'mon,tues,wed,thuds,fri'")
    


class Feedback(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

class Todayspecial(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6,decimal_places=6)


class Cheff(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    images = models.ImageField(upload_to="chefs")

class Subscribers(models.Model):
    email = models.EmailField(unique=True)
    Subscribed = models.DateTimeField(auto_now_add=True)


class MenuCategory(models.Model):
    name = models.CharField(max_length=100,unique=True)

class OrderStatus(models.Model):
    name = models.CharFields(max_length=100,unique=True)

class OrderItem(models.Model):
    status = models.ForeignKey(OrderStatus,on_delete=models.SET_NULL,nu8ll=true)
    name = models.CharField(max_length=100)
    quantity = models.PositiveInteger()
    price = models.DecimalField(max_length=8,decimal_places=2)
    
class ActiveOrderMange(models.Manage):
    def get_active_order(self):
        return self.filter(status__in=['pending','processing'])


python manage.py makemigration
python manage.py migrate