from django.urls import path
from . import views

urlpatterns = [
    path('signaler_panne/', views.signaler_panne, name='signaler_panne'),
]
