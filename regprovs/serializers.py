from rest_framework import serializers 
from rest_framework.validators import UniqueValidator 
from .models import Proveedor, Prod_Proveedor, Marca, Tipo, User
from django.db import transaction
from django.contrib.auth.hashers import make_password
from .mailjet import send_mailjet_email

class ProveedorSerializer(serializers.ModelSerializer):
    correo = serializers.EmailField(
        validators=[UniqueValidator(queryset=Proveedor.objects.all())]
    )

    class Meta:
        model = Proveedor
        fields = '__all__'

    def create(self, validated_data):
        with transaction.atomic():
            proveedor = Proveedor.objects.create(**validated_data)
            password = f"{proveedor.nombre}{proveedor.rut}"
            hashed_password = make_password(password) 
            link = "https://www.youtube.com/shorts/SXHMnicI6Pg"
            User.objects.create(
                username=proveedor.correo,
                password=hashed_password,
                rol='p',
                idproveedor=proveedor.id_proveedor
            )
            send_mailjet_email(
                email=proveedor.correo,
                name=proveedor.nombre,
                username=proveedor.correo,
                password=password,
                link=link
            )
        return proveedor

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