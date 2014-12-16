from rest_framework import serializers
from consulta.models import Localizar_CPF


class Localizar_CPFSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model  = Localizar_CPF
        fields = ('cpf', 'status')
