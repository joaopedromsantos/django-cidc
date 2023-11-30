from django.urls import include, path
from django.contrib import admin

from cadastros.views import ListaCidade, CidadeDetail, CidadeDelete, CidadeCreate, CidadeUpdate, ListaEstado, \
    EstadoDetail, EstadoDelete, EstadoUpdate, EstadoCreate

urlpatterns = [
    path('', ListaCidade.as_view(), name='cidades-list'), # url de listar cidades
    path('detalhe/<int:pk>/', CidadeDetail.as_view(), name='cidade-detalhe'), # url de detalhar a cidade escolhida
    path('delete/<int:pk>/', CidadeDelete.as_view(), name='cidades-remove'),
    path('update/<int:pk>/', CidadeUpdate.as_view(), name='cidades-editar'),
    path('create/', CidadeCreate.as_view(), name='cidades-cadastro'),

    path('estado/list/', ListaEstado.as_view(), name='estados-list'),
    path('estado/detalhe/<int:pk>/', EstadoDetail.as_view(), name='estado-detalhe'),
    path('estado/delete/<int:pk>/', EstadoDelete.as_view(), name='estado-remove'),
    path('estado/update/<int:pk>/', EstadoUpdate.as_view(), name='estados-editar'),
    path('estado/create/', EstadoCreate.as_view(), name='estados-cadastro'),
]
