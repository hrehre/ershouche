

from django.conf.urls import url

from APPS import views

urlpatterns = [
    url(r'index/', views.index, name='index'),
    url(r'error/',views.error, name='error')


]