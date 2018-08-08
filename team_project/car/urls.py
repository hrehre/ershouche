from django.conf.urls import url
from car import views

urlpatterns = [
    url(r'^member_center/',views.member_center,name='member_center'),
    url(r'^index/',views.index,name='index'),
    url(r'^my_request',views.my_request,name='my_request'),
    url(r'^account_manager/',views.account_manager,name='account_manager'),
    url(r'^list/',views.list,name='list'),
    url(r'^wymc/',views.wymc,name='wymc'),
]