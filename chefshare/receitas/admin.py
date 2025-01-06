from django.contrib import admin
from .models import Receita

@admin.register(Receita)
class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_criacao')  # Nome e Data de Criação
