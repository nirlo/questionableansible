from django.urls import path
from django.conf.urls import include, url
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$', views.homepage, name="homepage"),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^main/', include('questionableansible.urls')),
]

urlpatterns += staticfiles_urlpatterns()