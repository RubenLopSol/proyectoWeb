from django.urls import path
from .views import VRegistro, cerrar_session, VLogin



urlpatterns = [

   path('', VRegistro.as_view(), name="autenticacion"),

   path('cerrar_session', cerrar_session, name="cerrar_session"),

   path('login', VLogin, name="login"),
    
]

