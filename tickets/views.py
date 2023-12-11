from django.shortcuts import render, redirect
from django.views import View

from tickets.forms import NovaSolicitacaoForm


class NovaSolicitacao(View):

    def get(self, request):

        form = NovaSolicitacaoForm

        return render(request, 'tickets/form.html', {'form': form})

    def post(self, request):

        form = NovaSolicitacaoForm(request.POST, request.FILES)

        if form.is_valid():

            form.save()

            return redirect('cidades-list')

        return render(request, 'tickets/form.html', {'form': form})
