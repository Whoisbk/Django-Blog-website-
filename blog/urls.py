from django.urls import path 
from . import views

urlpatterns = [
    path('', views.home,name="home" ),
    path('signin/', views.signin,name="signin"),
    path('signout/', views.signout,name="signout"),
    path('register/', views.register,name="register"),
    path('profile/', views.profile,name="profile"),
    path('create/', views.create,name="create"),
    path('edit_profile/', views.edit_profile,name="edit_profile"),
]
