
from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse, request
from second_app.models import User
# Create your views here.

def index(request):
    mg_dict = {'insert_here':'WELCOME MR. KHAN'}
    return render(request,'second_app/index.html',context= mg_dict)

def users(request):
    user_list =User.objects.order_by('first_name')
    user_dict= {'users': user_list}
    return render(request,'second_app/users.html',context= user_dict)