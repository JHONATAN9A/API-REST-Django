from django.db import models

# Crear la estructura para el modelo de la base de datos de datos.
#Se crean las tablas para almacenar los datos de los inmuebles.


class Edificaciones(models.Model):
    #Creamos los campos de la tabla inmuebles
    direccion = models.CharField(max_length=255);
    pais = models.CharField(max_length=255);
    descripcion = models.CharField(max_length=255);
    imagen = models.CharField(max_length=255);
    active = models.BooleanField(default=True);
    created = models.DateTimeField(auto_now_add=True)
    
    #Retorna el id de la dirección
    def __str__(self):
        return self.direccion;

class Empresa(models.Model):
    nombre = models.CharField(max_length=255);
    website = models.URLField(max_length=255);
    active = models.BooleanField(default=True);
    
    def __str__(self):
        return self.nombre;