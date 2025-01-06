from django.db import models

class Receita(models.Model):
    nome = models.CharField(max_length=100)  # Nome da receita
    descricao = models.TextField(default='Sem descrição') # Descrição da receita
    ingredientes = models.TextField()  # Ingredientes
    instrucoes = models.TextField()
    modo_preparo = models.TextField(default='Sem infomação')  # Modo de preparo
    prep_time = models.IntegerField(help_text="Tempo de preparacao em minutos")
    data_criacao = models.DateTimeField(auto_now_add=True)  # Data de criação

    def __str__(self):
        return self.nome
