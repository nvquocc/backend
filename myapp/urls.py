from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login),
    path('register/', views.sign_up),
    path('student',views.show_student)

]
