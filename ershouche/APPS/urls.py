

from django.conf.urls import url

from APPS import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^index/register/', views.register, name='register'),
    url(r'^index/login/', views.login, name='login'),
    url(r'^error/',views.error, name='error')


]