from django.contrib.messages.views import SuccessMessageMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from cadastros.forms import CidadeForm, EstadoForm
from cadastros.models import Cidade, Estado


# Create your views here.

class ListaCidade(ListView):

    queryset = Cidade.objects.order_by('nome')
    context_object_name = 'cidades'
    template_name = 'cadastros/lista_cidades.html'


class CidadeDetail(DetailView):

    context_object_name = 'cidade'
    queryset = Cidade.objects.all()
    template_name = 'cadastros/detalhe_cidades.html'


class CidadeDelete(DeleteView):

    context_object_name = 'cidade'
    model = Cidade
    template_name = 'cadastros/remove_cidades.html'
    success_url = reverse_lazy('cidades-list')


class CidadeCreate(CreateView):
    form_class = CidadeForm
    template_name = 'cadastros/cadastra_cidades.html'
    success_url = reverse_lazy('cidades-list')


class CidadeUpdate(UpdateView, SuccessMessageMixin):
    model = Cidade
    form_class = CidadeForm
    template_name = 'cadastros/edita_cidades.html'
    success_url = reverse_lazy('cidades-list')
    success_message = 'Cadastro Atualizado com Sucesso'


class ListaEstado(ListView):
    queryset = Estado.objects.order_by('nome')
    context_object_name = 'estados'
    template_name = 'cadastros/lista_estados.html'


class EstadoDetail(DetailView):
    context_object_name = 'estado'
    queryset = Estado.objects.all()
    template_name = 'cadastros/detalhe_estado.html'


class EstadoDelete(DeleteView):
    context_object_name = 'estado'
    model = Estado
    template_name = 'cadastros/remove_estados.html'
    success_url = reverse_lazy('estados-list')


class EstadoUpdate(UpdateView, SuccessMessageMixin):
    model = Estado
    form_class = EstadoForm
    template_name = 'cadastros/edita_estados.html'
    success_url = reverse_lazy('estados-list')
    success_message = 'Cadastro Atualizado com Sucesso'


class EstadoCreate(CreateView):
    form_class = EstadoForm
    template_name = 'cadastros/cadastra_estados.html'
    success_url = reverse_lazy('estados-list')
