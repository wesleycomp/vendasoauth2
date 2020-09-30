from django.db import models

# Create your models here.
class Base(models.Model):
    criacao = models.DateTimeField(auto_now_add=True)
    atualizacao = models.DateTimeField(auto_now=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Produto(Base):
    descricao = models.CharField(max_length=100)
    unidade = models.CharField(max_length=10)
    genero = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.descricao

class Fornecedor(Base):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=20)
    endereco = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'

    def __str__(self):
        return self.nome