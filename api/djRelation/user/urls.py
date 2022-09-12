from django.conf.urls import url, include
from django.urls import path
from django.contrib import admin
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    path('user/',include('user/urls.py')),
]