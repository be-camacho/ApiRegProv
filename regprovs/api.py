from .models import Proveedor as P, Prod_Proveedor as PP, Tipo as T, Marca as M 
from rest_framework import viewsets, permissions
from .serializers import ProveedorSerializer as PS, Prod_ProveedorSerializer as PPS, TipoSerializer as TS, MarcaSerializer as MS
from rest_framework.renderers import JSONRenderer

class PViewSet(viewsets.ModelViewSet):
    queryset = P.objects.all()
    permission_classes = [permissions.AllowAny]#cambiar por IsAuthenticated en produccion
    serializer_class = PS
    renderer_classes = [JSONRenderer]

class PPViewSet(viewsets.ModelViewSet):
    queryset = PP.objects.all()
    permission_classes = [permissions.AllowAny]#cambiar por IsAuthenticated en produccion
    serializer_class = PPS
    renderer_classes = [JSONRenderer]

class TViewSet(viewsets.ModelViewSet):
    queryset = T.objects.all()
    permission_classes = [permissions.AllowAny]#cambiar por IsAuthenticated en produccion
    serializer_class = TS
    renderer_classes = [JSONRenderer]

class MViewSet(viewsets.ModelViewSet):
    queryset = M.objects.all()
    permission_classes = [permissions.AllowAny]#cambiar por IsAuthenticated en produccion
    serializer_class = MS
    renderer_classes = [JSONRenderer]