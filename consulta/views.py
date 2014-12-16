from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from consulta.serializers import Localizar_CPFSerializer
from consulta.models import Localizar_CPF


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from conectar.conectar import BuscaSipra
from rest_framework.parsers import XMLParser, JSONParser
from rest_framework.decorators import parser_classes



class Localizar_CPFViewSet(viewsets.ModelViewSet):
    parser_classes = (XMLParser, JSONParser)
    queryset = Localizar_CPF.objects.all()
    serializer_class = Localizar_CPFSerializer




@api_view(['GET', 'PUT', 'DELETE'])
@parser_classes((XMLParser, JSONParser))
def Localizar_CPF_detail(request, pk):
    """
    Retrieve, update or delete a Beneficiario.

    """

    b = BuscaSipra()
    s = b.busca_cpf(str(pk))
    lc = Localizar_CPF(cpf=str(pk),status=s)

    if request.method == 'GET':
        serializer = Localizar_CPFSerializer(lc)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Localizar_CPFSerializer(lc, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        lc.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
@parser_classes((XMLParser, JSONParser))
def Localizar_CPF2(request, pk):
    """
    Retrieve, update or delete a Beneficiario.

    """

    b = BuscaSipra()
    s = b.busca_cpf(str(pk))
    lc = Localizar_CPF(cpf=str(pk),status=s)

    return None
"""
    if request.method == 'GET':
        serializer = Localizar_CPFSerializer(lc)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Localizar_CPFSerializer(lc, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        lc.delete()
        return Response(status=status.HTTP_204_NO_CONTENT
"""
