from rest_framework import serializers
from inmueblesList_App.models import Edificacion,Empresa


class EdificacionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Edificacion
        fields = "__all__"
        #fields = ['direccion','pais','descripcion']
        #exclude =['id','imagen']

class EmpresaSerializer(serializers.ModelSerializer):
    edificacionlist =  EdificacionSerializer(many=True,read_only=True)
    #edificacionlist =  serializers.StringRelatedField(many=True)
    #edificacionlist =  serializers.PrimaryKeyRelatedField(many=True,read_only=True)
    # edificacionlist =  serializers.HyperlinkedRelatedField(
    #                     many=True,
    #                     read_only=True,
    #                     view_name="Edificación detalle"
    #                     )
    class Meta:
        model = Empresa
        fields = "__all__"

        
























    # def get_longitud_direccion(self, object):
    #     cantidad_caracteres = len(object.direccion)
    #     return cantidad_caracteres
    
    # def validate(self,data):
    #     if data['direccion'] == data['pais']:
    #         raise serializers.ValidationError('La direccion y el pais deben ser diferentes')
    #     else:
    #         return data





# def column_longitud(value):
#     if len(value) < 2:
#         raise serializers.ValidationError("La dirección es muy corta")

# class InmuebleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     direccion = serializers.CharField(validators=[column_longitud])
#     pais = serializers.CharField(validators=[column_longitud])
#     descripcion = serializers.CharField()
#     imagen = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self,validated_data):
#         return Inmueble.objects.create(**validated_data);
    
#     def update(self,instance,validated_data):
#         instance.direccion = validated_data.get('direccion',instance.direccion);
#         instance.pais = validated_data.get('pais',instance.pais);
#         instance.descripcion = validated_data.get('descripcion',instance.descripcion);
#         instance.imagen = validated_data.get('imagen',instance.imagen);
#         instance.active = validated_data.get('active',instance.active);
#         instance.save();
#         return instance;
    
#     def validate(self,data):
#         if data['direccion'] == data['pais']:
#             raise serializers.ValidationError('La direccion y el pais deben ser diferentes')
#         else:
#             return data
        