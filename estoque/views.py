from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import mixins
from .models import Produto, Fornecedor
from .serializers import ProdutoSerializer, FornecedorSerializer
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope, TokenHasScope
# Create your views here.
## ACRESCENTEI AO ARQUIVO para cadatro do usuario
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = "index.html"

class registrarUsuarioView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

class ProdutoViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
   ):
    permission_classes = [permissions.IsAuthenticated, TokenHasReadWriteScope]
   # permission_classes = (permissions.DjangoModelPermissions,)
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class FornecedorViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    viewsets.GenericViewSet
   ):

    permission_classes = (permissions.DjangoModelPermissions,)
    queryset = Fornecedor.objects.all()
    serializer_class = FornecedorSerializer

