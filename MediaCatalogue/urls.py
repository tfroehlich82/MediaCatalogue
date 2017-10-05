"""MediaCatalogue URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from media.views import IndexPage, ImagePage, VideoPage, AudioPage

urlpatterns = [
    url(r'^$', IndexPage.as_view(), name='index'),
    url(r'^images/$', ImagePage.as_view(), name='images'),
    url(r'^videos/$', VideoPage.as_view(), name='videos'),
    url(r'^audio/$', AudioPage.as_view(), name='audio'),
    url(r"^search/", include("watson.urls", namespace="watson")),
    url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),
    url(r'^admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
