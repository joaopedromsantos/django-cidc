from rest_framework import serializers

from tickets.models import Solicitacao


class SolicitacaoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Solicitacao
        fields = '__all__'