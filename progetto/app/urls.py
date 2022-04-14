from django.urls import path
from . import views
from app.views import clienti, sommaClienti

urlpatterns = [
    path('',views.index, name = 'index'),
    path('search/',clienti.as_view(),name='clienti_agente'),
    path('count/',sommaClienti.as_view(),name='count'),
]
