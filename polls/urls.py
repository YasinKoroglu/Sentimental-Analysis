


from django.urls import path
from polls import views
from . import views  
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings



urlpatterns  = [
    path('mainpage/' , views.simple_upload , name='mainpage'),
    path('mainpage/regulated/' , views.regulated , name='regulated'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)