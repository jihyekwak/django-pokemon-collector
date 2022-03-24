from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('index/', views.Index.as_view(), name="index"),
    path('index/new/', views.Create.as_view(), name="create"),
    path('index/<int:pk>/', views.Detail.as_view(), name="detail"),
    path('index/<int:pk>/update', views.Update.as_view(), name="update"),
    path('collection/', views.Collection.as_view(), name="collection"),
    path('user/<username>/', views.profile, name="profile"),
    path('users/', views.users, name="users")
]