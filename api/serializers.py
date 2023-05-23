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

    def create(self, validated_data):
        grossiste_data = validated_data.pop('grossiste')
        revendeur_data = validated_data.pop('revendeur')
        marchandise_data = validated_data.pop('marchandise')
        conditions_transport_data = validated_data.pop('conditions_transport')
        documents_data = validated_data.pop('documents')

        grossiste = Grossiste.objects.create(**grossiste_data)
        revendeur = Revendeur.objects.create(**revendeur_data)
        marchandise = Marchandise.objects.create(**marchandise_data)
        conditions_transport = ConditionTransport.objects.create(**conditions_transport_data)

        documents = []
        for document_data in documents_data:
            document = Document.objects.create(**document_data)
            documents.append(document)

        transport = Transport.objects.create(
            grossiste=grossiste,
            revendeur=revendeur,
            marchandise=marchandise,
            conditions_transport=conditions_transport,
            **validated_data
        )

        transport.documents.set(documents)

        return transport
