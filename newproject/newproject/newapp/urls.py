from django.urls import path
from . import views

app_name='newapp'
urlpatterns = [

    path('home',views.home,name='home'),
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('new', views.new, name='new'),
    path('form', views.form, name='form'),
    path('logout', views.logout, name='logout'),


]