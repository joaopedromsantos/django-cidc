from django import forms

from cadastros.models import Cidade, Estado


class CidadeForm(forms.ModelForm):

    class Meta:
        model = Cidade
        fields = '__all__'


class EstadoForm(forms.ModelForm):

    class Meta:
        model = Estado
        fields = '__all__'