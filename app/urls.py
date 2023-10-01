from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('login',views.auth_login),
    path('logout',views.auth_logout)
]