from django.conf.urls import url 
from . import views

app_name = 'questionableansible'

urlpatterns = [
    url(r'^$', views.Main, name="main"),
    url(r'^create/', views.Create, name="create"),
    url(r'^credentials/$', views.Credentials, name="credentials"),

]