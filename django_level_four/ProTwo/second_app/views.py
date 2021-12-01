
from django.shortcuts import render
from django.urls import path
from django.http import HttpResponse, request
#from second_app.models import User
#from second_app.forms import FormName
from second_app.forms import  NewUserForm
from second_app import forms
# Create your views here.

def index(request):
    mg_dict = {'insert_here':'WELCOME MR. KHAN'}
    return render(request,'second_app/index.html',context= mg_dict)
""" 
def form_name_view(request):
    form = forms.FormName()
    if request.method == 'POST':
        form= forms.FormName(request.POST)
    
    if form.is_valid():
        print('validation success!')
        print('Name: '+form.cleaned_data['name'])
        print('age: '+str(form.cleaned_data['age']))
        print('Email: '+form.cleaned_data['email'])
        print('comments: '+form.cleaned_data['comments'])
    return render(request,'second_app/forms.html',{'form':form}) """


def users(request):
    form = NewUserForm()
    if request.method == 'POST':
        form = NewUserForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return index(request)
        else:
            print('invalid details')
    return render(request,'second_app/forms.html',{'form':form})