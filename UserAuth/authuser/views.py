import email
from email import message
import json
from lib2to3.pgen2 import token
from tkinter import FLAT
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import userdata
from .serailizers import userdataSerializer
import io
from django.http import HttpResponse,JsonResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import uuid
from django.core.mail import send_mail,send_mass_mail
from django.conf import settings
from django.contrib import messages
# Create your views here.
@csrf_exempt
def home(request):
    return render(request,'reg.html')
@csrf_exempt
def reg(request):
    if request.method == 'POST':
        json_data=request.body
        stream = io.BytesIO(json_data)
        
        pythondata=JSONParser().parse(stream)
        # print("uuid is sss",uid)
        # print(pythondata)
    serializer = userdataSerializer(data=pythondata)
    if serializer.is_valid():
            # print("line22")
            serializer.save()
            # obj=userdata.objects.values_list('id',flat=True)
            # userdata.objects.filter(email=pythondata['email']).update(verify=True)
            uid=uuid.uuid4()
            userdata.objects.filter(email=pythondata['email']).update(token=uid)
            # print(obj)
            send_mail_reg(pythondata['email'],uid)
            messages.success(request,"check your mail")
            res = {'msg':'data created'}
            # json_data = JSONRenderer().render(res)
            json_data = json.dumps(res)
            print("Json data is",json_data)
            return redirect('/reg')
            # return HttpResponse(json_data, content_type='application/json')
    res = {'msg':'data not created'}
    json_data = JSONRenderer().render(res)
    print(json_data)
    return HttpResponse(json_data, content_type='application/json')
        

def sign(request):
    return render(request, "sign.html")


def acc_verify(request,token):
    print("token is",token)
    userdata.objects.filter(token=token).update(verify=True)
    return HttpResponse("your account verify")




def send_mail_reg(email, token):
    print("email call")
    subject= "Verify email"
    message= f'Please click on the link to verify account http://127.0.0.1:8000/acc_verify/{token}'
    from_email = settings.EMAIL_HOST_USER
    recipient_list=[email]
    # fail_silently=False,
    print("dataseted")
    send_mail(subject=subject, message=message, from_email=from_email, recipient_list=recipient_list)
    # message1 = ('Subject here', 'Here is the message', 'atul.rana2707@gmail.com', ['ranaatul9211@gmail.com'])
    # message2 = ('Another Subject', 'Here is another message', 'from@example.com', ['second@test.com'])
    # send_mass_mail((message1), fail_silently=False)

@csrf_exempt
def signuser(request):
    print("signuserrcall")
    if request.method == 'POST':
        json_data=request.body
        stream = io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        # userdata.objects.filter(email=pythondata['email']).get('verify', FLAT)
        # obj=userdata.objects.values_list('email',flat=True)
        dbpass = userdata.objects.filter(email=pythondata['email']).values_list('password',flat=True)
        dbverify = userdata.objects.filter(email=pythondata['email']).values_list('verify',flat=True)
        if dbverify[0] == False:
            print("pls verify your account before login")
            return HttpResponse("your account in not verified")
        else:
            if dbpass[0]==pythondata['password']:
                print("You have successfully logedin")
                return HttpResponse("you login")
            else:
                print("Login failed bad credentials")
                return HttpResponse("pls enter correct username and password")


    
