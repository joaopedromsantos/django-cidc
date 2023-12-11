from rest_framework import serializers

from cadastros.models import Cidade


class CidadeSerializer(serializers.ModelSerializer):

    estado_nome = serializers.ReadOnlyField(source='estado.nome')
    pais_nome = serializers.ReadOnlyField(source='estado.pais.nome')

    class Meta:
        model = Cidade
        fields = ['id', 'pais_nome', 'estado_nome', 'nome', 'capital', 'descricao']


class TestSerializer(serializers.Serializer):

    nome = serializers.CharField(max_length=45)