from django.urls import path

from sayt_dashboard.category.views import *
from sayt_dashboard.views import *
from sayt_dashboard.product.views import *


urlpatterns = [
    path('', index, name='dashboard-home'),
    path('ctg/list/', ctg_list, name='dashboard-ctg-list'),
    path('ctg/detail/<int:pk>/', ctg_detail, name='dashboard-ctg-detail'),
    path('ctg/delete/<int:pk>/', ctg_delete, name='dashboard-ctg-delete'),
    path('ctg/add/', ctg_add, name='dashboard-ctg-add'),
    path('ctg/edit/<int:pk>', ctg_edit, name='dashboard-ctg-edit'),
    path('ctg/confirm/<int:pk>', ctg_confirm, name='dashboard-ctg-confirm'),

    path('product/list/', list_product, name='dashboard-pro-list'),
    path('product/add/', add_product, name='dashboard-pro-add'),
    path('product/detail/<int:pk>/', detail_product, name='dashboard-pro-detail'),
    path('product/edit/<int:pk>', edit_product, name='dashboard-pro-edit'),
    path('prodyct/delete/<int:pk>/', delete_product, name='dashboard-pro-delete'),


    path('dashboard/logout', dash_logout, name='dashboard-logout'),
    path('dashboard/login', dash_login, name='dashboard-login'),
    path('dashboard/register', dash_register, name="dashboardi-register")

]