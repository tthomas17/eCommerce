from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
    url(r'^admin/', admin.site.urls ),
    url (r'^accounts/', include('registration.backends.default.urls')),
    url (r'^products/', include('products.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)