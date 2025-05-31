from django.urls import re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.urls import include, path

schema_view = get_schema_view(
   openapi.Info(
      title="API PROVEEDORES",
      default_version='v1',
      description="apis de proveedores",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="noemail@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('regprovs.urls')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redocs/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
