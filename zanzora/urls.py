from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [path("admin/", admin.site.urls), path("", include("explore.urls"))]

# Fallback static-file route for the Render Gunicorn deployment.
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
