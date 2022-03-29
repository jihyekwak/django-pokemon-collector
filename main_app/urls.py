from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('about/', views.About.as_view(), name="about"),
    path('index/', views.Index.as_view(), name="index"),
    path('index/new/', views.Create.as_view(), name="create"),
    path('index/<int:pk>/', views.Detail.as_view(), name="detail"),
    path('index/<int:pk>/update', views.Update.as_view(), name="update"),

    path('users/', views.users, name="users"),
    path('user/<username>/', views.profile, name="profile"),

    path('moves/', views.moves_index, name="moves_index"),
    path('moves/<int:move_id>/', views.move_show, name="move_show"),
    path('moves/new', views.Move_Create.as_view(), name="move_create"),
    path('moves/<int:pk>/update', views.Move_Update.as_view(), name="move_update"),
    path('moves/<int:pk>/delete', views.Move_Delete.as_view(), name="move_delete"),

    path('leagues/', views.leagues_index, name="leagues_index"),
    # path('leagues/<int:league_id>/', views.league_show, name="league_show"),
    path('leagues/new', views.League_Create.as_view(), name="league_create"),
    path('leagues/<int:pk>/update', views.League_Update.as_view(), name="league_update"),
    path('leagues/<int:pk>/delete', views.League_Delete.as_view(), name="league_delete"),
]