# Generated by Django 4.0.5 on 2022-06-28 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inmueble',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('direccion', models.CharField(max_length=255)),
                ('pais', models.CharField(max_length=255)),
                ('descripcion', models.CharField(max_length=255)),
                ('imagen', models.CharField(max_length=255)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
