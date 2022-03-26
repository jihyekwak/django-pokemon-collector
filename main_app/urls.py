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
    path('users/', views.users, name="users"),
    path('battles/', views.battles_index, name="battles_index"),
    path('battles/<int:battle_id>/', views.battle_show, name="battle_show"),
    path('battles/new', views.Battle_Create.as_view(), name="battle_create"),
    path('batttles/<int:pk>/update', views.Battle_Update.as_view(), name="battle_update"),
    path('battles/<int:pk>/delete', views.Battle_Delete.as_view(), name="battle_delete")
]