from django.urls import path
from .views import *

urlpatterns = [
    path['',views.homepage,name='homepage']
    path('about',views.aboutpage,name='aboutpage')
]