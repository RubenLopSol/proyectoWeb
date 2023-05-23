from django.urls import path

from .views import servicios
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [


    path('servicios/', servicios, name="servicios"),

    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)