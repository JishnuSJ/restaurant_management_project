from django.urls import path
from .views import *

urlpatterns = [
    path('',views.homepage,name='homepage'),
    path('about',views.aboutpage,name='aboutpage'),
    path('menu',views.menu_list,name='menu'),
    path('privacy-policy'.views.privacy-policy,name='privacy-policy')
]