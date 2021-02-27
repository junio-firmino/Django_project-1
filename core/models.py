from django.db import models

class Produto(models.Model):
    nome = models.CharField('nome', max_length=100)
    preco = models.DecimalField('Preço', max_digits=5, decimal_places=2)
    estoque = models.IntegerField('Quantidade de estoques')
