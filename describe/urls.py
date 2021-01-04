from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('describe/', views.login, name='login'),
    path('<int:placeholder>', views.login_submit, name='login_submit'),
    path('describe/<username>/', views.index, name='index'),
    path('<int:class_id>/', views.submit, name='submit'),
]