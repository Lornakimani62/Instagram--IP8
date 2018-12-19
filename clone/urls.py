from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url('^$' , views.home, name='home'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^image/(\d+)',views.image,name ='image'),
    url(r'^search/', views.search, name='search'),
    url(r'^upload/', views.upload, name='upload'),
    ]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)