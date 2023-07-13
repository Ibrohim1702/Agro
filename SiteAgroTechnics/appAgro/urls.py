from django.urls import path

from appAgro.views import *

urlpatterns = [

    path('', index, name='home'),
    path('views/<int:pk>', views, name='views'),
    path('register/', agrologin, name='register'),
    path('category/<slug>/', category, name='category'),
    path('category', category, name='category'),
    path('search', search_products, name='search'),

]