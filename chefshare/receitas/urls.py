from django.urls import path
from . import views

urlpatterns = [
    path('', views.receitas_list, name='receitas_list'),
]