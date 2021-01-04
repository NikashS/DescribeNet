from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:class_id>/', views.submit, name='submit'),
    # path('<int:class_id>/', views.describe, name='describe'),
]