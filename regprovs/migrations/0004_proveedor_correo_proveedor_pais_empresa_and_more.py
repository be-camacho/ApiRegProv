# Generated by Django 5.2 on 2025-05-01 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regprovs', '0003_alter_prod_proveedor_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='correo',
            field=models.EmailField(default='sin-correo@example.com', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proveedor',
            name='pais_empresa',
            field=models.CharField(default='usa', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proveedor',
            name='telefono',
            field=models.CharField(default='+569133133', max_length=15),
            preserve_default=False,
        ),
    ]
