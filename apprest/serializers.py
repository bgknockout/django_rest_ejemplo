from rest_framework import serializers
from .models import Cliente

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        #Campos json
        fields = ('url', 'rut', 'nombre','apellido', 'direccion', 'edad')