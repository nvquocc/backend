from http.client import HTTPResponse
from django.shortcuts import render
from myapp.models import Employee


# Create your views here.

def login(request):
    return render(request, 'login.html')


def sign_up(request):
    return render(request, 'signup.html')


def show_employee(request):
    context = {'employees': Employee.objects.all()}
    return render(request, 'employee/index.html', context)


def add_employee(request):
    print("add")