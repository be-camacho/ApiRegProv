from rest_framework import serializers 
from .models import Proveedor, Prod_Proveedor, Marca, Tipo

class ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
        fields = '__all__'

class Prod_ProveedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prod_Proveedor
        fields = '__all__'

class MarcaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marca
        fields = '__all__'

class TipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo
        fields = '__all__'