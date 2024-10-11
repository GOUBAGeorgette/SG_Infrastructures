from django.contrib import admin
from django.urls import path, include
from infra_track import views  # Assurez-vous d'importer correctement les vues

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Route pour la page d'accueil
    path('signaler_panne/', include('infra_track.urls')),  # Vérifiez que cette ligne est correcte
]
