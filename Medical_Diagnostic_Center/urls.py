# Medical_Diagnostic_Center/urls.py

from django.conf.urls.static import static
from clinic import views as clinic_views
from django.urls import include, path
from django.conf import settings
from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', clinic_views.index, name='index'),
    path('appointments/', include('appointments.urls', namespace='appointments')),
    path('authentication/', include('authentication.urls', namespace='authentication')),
    path('clinic/', include('clinic.urls', namespace='clinic')),
    path('feedback/', include('feedback.urls', namespace='feedback')),
    path('educational_resources/', include('educational_resources.urls', namespace='educational_resources')),
    path('online_consultations/', include('online_consultations.urls', namespace='online_consultations')),
    path('summernote/', include('django_summernote.urls')),
    # Добавьте другие пути приложений здесь
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
