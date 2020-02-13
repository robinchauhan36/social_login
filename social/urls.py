from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from login import views as login_views

urlpatterns = [
    url(r'^$', login_views.home, name='home'),
    url(r'^login/$', auth_views.LoginView, name='login'),
    url(r'^logout/$', auth_views.LogoutView, name='logout'),
    url(r'^oauth/', include('social_django.urls', namespace='social')),
    path('admin/', admin.site.urls),
]
