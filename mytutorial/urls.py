# tutorial/urls.py
from django.contrib import admin
from django.urls import include, path  # new
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', RedirectView.as_view(url='/snippets/', permanent=False)),
    path('', include('snippets.urls')),
    path("api-auth/", include("rest_framework.urls"))
]