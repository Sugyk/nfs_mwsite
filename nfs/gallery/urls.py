from django.urls import path
from .views import CarListView, UserCreateView, LoginUser, LogoutUser, BrandListView, ProfileView, ProfileEdit


urlpatterns = [
    path('', CarListView.as_view(), name='car_list'),
    path('reg/', UserCreateView.as_view(), name='reg'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutUser.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('brand/<int:brand_id>', BrandListView.as_view(), name='brand_order'),
    path('profile/update/', ProfileEdit.as_view(), name='profile_update'),
]