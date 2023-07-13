from django.urls import path

from api.v1.category.views import CategoryView
from api.v1.dashboard.User.views import RegisterView, LoginView, LogoutView
from api.v1.product.views import ProductView

urlpatterns = [

    path('pro/list/', ProductView.as_view(), name='pro_list'),
    path('pro/list/<int:pk>/', ProductView.as_view(), name='pro_one'),

    path('ctg/list/', CategoryView.as_view(), name='ctg_ist'),
    path('ctg/list/<int:pk>/', CategoryView.as_view(), name='ctg_one'),

    path('auth/register/', RegisterView.as_view(), name="api_register"),
    path('auth/login/', LoginView.as_view(), name="api_login"),
    path('auth/loginout/', LogoutView.as_view(), name="api_logout")

]
