from .models import Proveedor as P, Prod_Proveedor as PP, Tipo as T, Marca as M 
from rest_framework import viewsets, permissions
from .serializers import ProveedorSerializer as PS, Prod_ProveedorSerializer as PPS, TipoSerializer as TS, MarcaSerializer as MS

class PViewSet(viewsets.ModelViewSet):
    queryset = P.objects.all()
    permission_classes = [permissions.AllowAny]#cambiar por IsAuthenticated en produccion
    serializer_class = PS

class PPViewSet(viewsets.ModelViewSet):
    queryset = PP.objects.all()
    permission_classes = [permissions.AllowAny]#cambiar por IsAuthenticated en produccion
    serializer_class = PPS

class TViewSet(viewsets.ModelViewSet):
    queryset = T.objects.all()
    permission_classes = [permissions.AllowAny]#cambiar por IsAuthenticated en produccion
    serializer_class = TS

class MViewSet(viewsets.ModelViewSet):
    queryset = M.objects.all()
    permission_classes = [permissions.AllowAny]#cambiar por IsAuthenticated en produccion
    serializer_class = MS