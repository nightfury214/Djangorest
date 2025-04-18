
from django.contrib import admin
from django.urls import include, path, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import renderers, permissions

scheme_view = get_schema_view(
    openapi.Info(
        title="Your API Title",
        default_version='v1',
        description="API documentation usin swagger 2.0",
        terms_of_service="https://www.example.com/terms",
        contact=openapi.Contact(email="contract@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny]

)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('snippets.urls')),
    path("api-auth/", include("rest_framework.urls")),
    # swaggerUI
    re_path(r'^swagger/$', scheme_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    # ReDoc UI
    re_path(r'^redoc/$', scheme_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
]