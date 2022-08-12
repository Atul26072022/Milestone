from django.contrib import admin
from django.urls import path
from  .views import *

urlpatterns = [
    
	path('', notification_push, name='push_notification'),
    
]
  