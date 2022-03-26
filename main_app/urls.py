from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('index/', views.Index.as_view(), name="index"),
    path('index/new/', views.Create.as_view(), name="create"),
    path('index/<int:pk>/', views.Detail.as_view(), name="detail"),
    path('index/<int:pk>/update', views.Update.as_view(), name="update"),
    path('user/<username>/', views.profile, name="profile"),
    path('users/', views.users, name="users"),
    path('leagues/', views.leagues_index, name="leagues_index"),
    path('leagues/<int:league_id>/', views.league_show, name="league_show"),
    path('leagues/new', views.League_Create.as_view(), name="league_create"),
    path('leagues/<int:pk>/update', views.League_Update.as_view(), name="league_update"),
    path('leagues/<int:pk>/delete', views.League_Delete.as_view(), name="league_delete")
]