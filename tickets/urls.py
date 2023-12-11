from django.urls import path

from tickets.apis import SolicitacaoAPIView
from tickets.views import NovaSolicitacao

urlpatterns = [
    path('tickets/', NovaSolicitacao.as_view(), name='nova-solicitacao-ticket'),
    path('tickets/api', SolicitacaoAPIView.as_view(), name='solicitacao-api-ticket'),
]
