from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.view_details, name='index'),
    url(r'^edit/$', views.edit_details, name='edit_details'),
    url(r'^change_password/$', views.change_password, name='change_password'),
]
