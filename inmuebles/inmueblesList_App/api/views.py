from rest_framework.response import Response
#from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import status
from inmueblesList_App.models import Edificaciones,Empresa
from inmueblesList_App.api.serializer import EdificacionSerializer,EmpresaSerializer


class EmpresaListAV(APIView):
    def get(self, request):
        empresas = Empresa.objects.all();
        serializer = EmpresaSerializer(empresas,many=True);
        return Response(serializer.data);
    
    def post(self, request):
        serializer = EmpresaSerializer(data=request.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data);
        else:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND);

class EdificacionListAV(APIView):
    def get(self, request):
        inmuebles = Edificaciones.objects.all();
        serializer = EdificacionSerializer(inmuebles,many=True);
        return Response(serializer.data);
    
    def post(self, request):
        serializer = EdificacionSerializer(data=request.data);
        if serializer.is_valid():
            serializer.save();
            return Response(serializer.data);
        else:
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND);
    

class EdificacionDetalleAV(APIView):
    def get(self, request, pk):        
        try:
            inmueble = Edificaciones.objects.get(pk=pk);
            serializer = EdificacionSerializer(inmueble);
            return Response(serializer.data)
        except Edificaciones.DoesNotExist:
            return Response({'Error':'No existe el inmueble'},status=status.HTTP_404_NOT_FOUND);
    
    def put(self, request, pk):
        inmueble = Edificaciones.objects.get(pk=pk);
        de_serializer = EdificacionSerializer(inmueble,data=request.data);
        if de_serializer.is_valid():
            de_serializer.save();
            return Response(de_serializer.data);
        else:
            return Response(de_serializer.errors,status=status.HTTP_400_BAD_REQUEST);
    
    def delete(self, request, pk):
        try:
            inmueble = Edificaciones.objects.get(pk=pk);
            inmueble.delete();
            return Response(status=status.HTTP_204_NO_CONTENT);
        except Edificaciones.DoesNotExist:
            return Response({'Error':'No existe el inmueble'},status=status.HTTP_404_NOT_FOUND);






# @api_view(['GET','POST'])
# def inmueble_list(request):
#     if request.method == 'GET':
#         inmuebles = Inmueble.objects.all();
#         serializer = InmuebleSerializer(inmuebles,many=True);
#         return Response(serializer.data);
#     if request.method == 'POST':
#         de_serializer = InmuebleSerializer(data=request.data);
#         if de_serializer.is_valid():
#             de_serializer.save();
#             return Response(de_serializer.data);
#         else:
#             return Response(de_serializer.errors);

# @api_view(['GET','PUT','DELETE'])
# def inmueble_detalle(request,pk):
#     if request.method == 'GET':
#         try:
#             inmueble = Inmueble.objects.get(pk=pk);
#             serializer = InmuebleSerializer(inmueble);
#             return Response(serializer.data)
#         except Inmueble.DoesNotExist:
#             return Response({'Error':'No existe el inmueble'},status=status.HTTP_404_NOT_FOUND)
        
#     if request.method == 'PUT':
#         inmueble = Inmueble.objects.get(pk=pk);
#         de_serializer = InmuebleSerializer(inmueble,data=request.data);
#         if de_serializer.is_valid():
#             de_serializer.save();
#             return Response(de_serializer.data);
#         else:
#             return Response(de_serializer.errors,status=status.HTTP_400_BAD_REQUEST);
    
#     if request.method == 'DELETE':
#         try:
#             inmueble = Inmueble.objects.get(pk=pk);
#             inmueble.delete();
#             return Response(status=status.HTTP_204_NO_CONTENT);
#         except Inmueble.DoesNotExist:
#             return Response({'Error':'No existe el inmueble'},status=status.HTTP_404_NOT_FOUND);