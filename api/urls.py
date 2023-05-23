from django.urls import path
from . import views

urlpatterns = [
    path('epcis/', views.transport_view, name='transport'),
]
