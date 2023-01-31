from django.urls import path
from .views import CarListView, UserCreateView, LoginUser, LogoutUser, BrandListView


urlpatterns = [
    path('', CarListView.as_view(), name='car_list'),
    path('reg/', UserCreateView.as_view(), name='reg'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutUser.as_view(), name='logoout'),
    path('brand/<int:brand_id>', BrandListView.as_view(), name='brand_order')
]