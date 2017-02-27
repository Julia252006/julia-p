from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.views import login, logout
from shared_templates import views


urlpatterns = [
    url(r'^$', views.login_redirect, name='login_redirect'),
    url(r'^admin/', admin.site.urls),
    url(r'^home/', include('home.urls')),
    url(r'^login/', login, {'template_name': 'login.html'}),
    url(r'^logout/', logout, {'template_name': 'logout.html'}),
    url(r'^register/', include('register.urls')),
    url(r'^details/', include('details.urls')),
]
