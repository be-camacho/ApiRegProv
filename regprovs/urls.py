from rest_framework import routers as RT
from .api import ProveedorViewSet as PVS, Prod_ProveedorViewSet as PPVS, TipoViewSet as TVS, MarcaViewSet as MVS

RT = RT.DefaultRouter()

RT.register('api/proveedor',PVS,'Proveedor')
RT.register('api/prod_proveedor',PPVS,'Producto Proveedor')
RT.register('api/tipo',TVS,'Tipo')
RT.register('api/marca',MVS,'Marca')

urlpatterns = RT.urls