from rest_framework import serializers
from .models import Produto, Fornecedor

class ProdutoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Produto
        fields = (
            'id',
            'descricao',
            'unidade',
            'genero',
            'criacao',
            'atualizacao',
            'ativo'
     )

class FornecedorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Fornecedor
        fields = (
            'id',
            'nome',
            'cnpj',
            'criacao',
            'atualizacao',
            'ativo'
        )