from django.contrib import admin
from django.urls import path
from  .views import *


# urls of payment_app
urlpatterns = [
    # razorpay_demo_url
	path('', razorpay_payment, name='home'),
    # url of success page for payment verification
    path('success' , success , name='success')
]
