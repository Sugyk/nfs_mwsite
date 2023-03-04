from django.urls import path
from .views import (
    CarListView, UserCreateView, LoginUser, LogoutUser,
    BrandListView, ProfileView, ProfileEdit, CarView, ArticleCreateView,
    ArticleView, ArticleEditView, ArticleList, AddNoteView
    )


urlpatterns = [
    path('', CarListView.as_view(), name='car_list'),
    path('<int:pk>', CarView.as_view(), name='car'),

    path('<int:pk>/create', ArticleCreateView.as_view(), name='new_article'),
    path('article/<int:pk>', ArticleView.as_view(), name='article'),
    path('articles/car/<int:pk>', ArticleList.as_view(), name='article_list'),

    path('article/<int:pk>/edit', ArticleEditView.as_view(), name='article_edit'),
    path('article/<int:pk>/new_note', AddNoteView.as_view(), name='article_new_note'),
    
    path('brand/<int:brand_id>', BrandListView.as_view(), name='brand_order'),
    
    path('reg/', UserCreateView.as_view(), name='reg'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutUser.as_view(), name='logout'),

    path('profile/<int:pk>', ProfileView.as_view(), name='profile'),
    path('profile/update/', ProfileEdit.as_view(), name='profile_update'),
]
