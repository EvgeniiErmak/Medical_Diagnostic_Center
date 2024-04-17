# Medical_Diagnostic_Center/urls.py

from django.conf.urls.static import static
from clinic import views as clinic_views
from django.urls import include, path
from django.conf import settings
from django.contrib import admin
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="API Docs",
        default_version='v1',
        description="API documentation for Medical Diagnostic Center",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', clinic_views.index, name='index'),
    path('appointments/', include('appointments.urls', namespace='appointments')),
    path('authentication/', include('authentication.urls', namespace='authentication')),
    path('clinic/', include('clinic.urls', namespace='clinic')),
    path('feedback/', include('feedback.urls', namespace='feedback')),
    path('educational_resources/', include('educational_resources.urls',
         namespace='educational_resources')),
    path('online_consultations/', include('online_consultations.urls',
         namespace='online_consultations')),
    path('summernote/', include('django_summernote.urls')),
    path('swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
