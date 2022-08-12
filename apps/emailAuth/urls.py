from django.contrib import admin
from django.urls import path, include
from .import views
urlpatterns = [
    path('',views.home),
    path('reg/', views.reg),
    path('sign/', views.sign),
    path('acc_verify/<slug:token>',views.acc_verify),
    path('signuser/', views.signuser),
    path('sms/', views.sms),
]