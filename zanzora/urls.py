from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.views import serve as serve_static
from django.urls import include, path
from django.urls import re_path

urlpatterns = [path("admin/", admin.site.urls), path("", include("explore.urls"))]

# Fallback static-file route for the Render Gunicorn deployment.
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Vercel routes requests through the Django function when a CDN asset is not
# available. Serve the source static files in that function as a reliable
# fallback; Vercel's filesystem route still serves CDN assets first.
if settings.IS_VERCEL:
    urlpatterns += [
        re_path(r"^static/(?P<path>.*)$", serve_static, {"insecure": True}),
    ]
