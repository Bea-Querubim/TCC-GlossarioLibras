from django.conf import settings
from django.contrib import *
from django.urls import path, include
from glossarioLibras import urls as glossario_urls
from .views import *
from . import views
from django.conf.urls.static import static
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home, name='home'),
    path('#about',home, name='about'),
    path('#contact',home, name='contact'),
    path('glossario/',include(glossario_urls), name='glossario'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('accounts/login',views.login, name="login"),
    path('accounts/sign',views.sign, name="sign"),
    path('accounts/logout', logout_view, name='logout'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
