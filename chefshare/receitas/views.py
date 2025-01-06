from django.shortcuts import render
from .models import Receita
from django.http import HttpResponse

def receitas_list(request):
    receitas = Receita.objects.all()
    return render(request, 'receitas/receitas_list.html', {'receitas': receitas})

def index(request):
    receitas = Receita.objects.all()[:10]  # Busca as 10 primeiras receitas
    return render(request, 'receitas/index.html', {'receitas': receitas})
