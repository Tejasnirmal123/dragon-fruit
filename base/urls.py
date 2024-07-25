from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name='home_view'),
    path('order/', order_view, name='order_view'),
    path('success/', order_success, name='order_success'),
    path('login/', login_view, name='login_view')
]