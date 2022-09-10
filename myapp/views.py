from django.shortcuts import render
from django.http import HttpRequest


# Create your views here.

def login(request):
    return render(request, 'login.html')


def sign_up(request):
    return render(request, 'signup.html')


def show_student(request):
    return render(request, 'student/student.html')
