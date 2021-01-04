from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('describe/', views.login, name='login'),
    path('login_submit/', views.login_submit, name='login_submit'),
    path('describe/<username>/', views.describe, name='describe'),
    path('describe_submit/', views.describe_submit, name='describe_submit'),
]