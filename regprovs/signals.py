from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.hashers import make_password
from .models import Proveedor, User
from .mailjet import send_mailjet_email
import datetime
link = "https://www.youtube.com/shorts/SXHMnicI6Pg"

@receiver(post_save, sender=Proveedor)
def crear_usuario_proveedor(sender, instance, created, **kwargs):
    if created:
        # Generar username
        fecha_actual = datetime.datetime.now()
        username = (
            f"{instance.nombre.lower()}."
            f"{instance.apellido[:2].lower()}."
            f"{fecha_actual.day:02}{fecha_actual.month:02}."
            f"{instance.dv}"
        )
        
        # Generar password
        password = (
            f"{instance.nombre[:3].lower()}"
            f"{instance.rut // 5}"
            f"{fecha_actual.day * fecha_actual.month}"
        )
        # Eviar correo
        response = send_mailjet_email(
            instance.correo,
            instance.nombre,
            username,
            password,
            link
        )
        print("Status Code:", response["status_code"])
        print("Respuesta de Mailjet:", response["response"])
        # Crear usuario
        User.objects.create(
            username=username,
            password=make_password(password),
            idproveedor=instance.id_proveedor,
            rol='p'
        )