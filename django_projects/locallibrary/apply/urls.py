from django.urls import path
from apply import views

urlpatterns = [
    path('', views.index, name='index2'),
]
