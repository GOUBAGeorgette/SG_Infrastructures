from django.urls import path
from .views import signaler_panne

urlpatterns = [
    path('signaler_panne/', signaler_panne, name='signaler_panne'),
]
