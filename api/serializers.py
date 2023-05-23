from rest_framework import serializers
from .models import Grossiste, Revendeur, Marchandise, ConditionTransport, Document, Transport

class GrossisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grossiste
        fields = '__all__'


class RevendeurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revendeur
        fields = '__all__'


class MarchandiseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marchandise
        fields = '__all__'


class ConditionTransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConditionTransport
        fields = '__all__'


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'


class TransportSerializer(serializers.ModelSerializer):
    grossiste = GrossisteSerializer()
    revendeur = RevendeurSerializer()
    marchandise = MarchandiseSerializer()
    conditions_transport = ConditionTransportSerializer()
    documents = DocumentSerializer(many=True)

    class Meta:
        model = Transport
        fields = '__all__'
