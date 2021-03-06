"""kinocms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from . import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
                  path('djadmin/', admin.site.urls),
                  path('', include('kino.urls')),
                  path('profile/', include('django.contrib.auth.urls')),
                  path('profile/', include('register.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
