from django.contrib import admin
from django.urls import path, include  # N'oublie pas d'importer include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('infra_track.urls')),  # Inclut les URLs de infra_track
]
