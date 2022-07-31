from django.urls import path
#from inmueblesList_App.api.views import inmueble_list,inmueble_detalle
from inmueblesList_App.api.views import EdificacionListAV,EdificacionDetalleAV,EmpresaListAV


urlpatterns = [
    path('edificacion/', EdificacionListAV.as_view(), name="Lista de edificaciones"),
    path('edificacion/<int:pk>', EdificacionDetalleAV.as_view(), name="Edificación detalle"),
    path('empresa/', EmpresaListAV.as_view(), name="Lista de empresas"),
]