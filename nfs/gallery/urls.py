from django.urls import path
from .views import (
    CarListView, UserCreateView, LoginUser, LogoutUser,
    BrandListView, ProfileView, ProfileEdit, CarView, ArticleCreateView, ArticleReadView

    )


urlpatterns = [
    path('', CarListView.as_view(), name='car_list'),
    path('<int:pk>', CarView.as_view(), name='car'),
    path('<int:pk>/create', ArticleCreateView.as_view(), name='new_article'),
    path('article/<int:pk>', ArticleReadView.as_view(), name='article'),
    # path('<int:pk>/create', testsave, name='new_article'),
    path('brand/<int:brand_id>', BrandListView.as_view(), name='brand_order'),
    

    path('reg/', UserCreateView.as_view(), name='reg'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutUser.as_view(), name='logout'),

    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('profile/update/', ProfileEdit.as_view(), name='profile_update'),
]
