from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.wechat,name='wechat'),
    url(r'create^$', views.create_menu,name='create'),
]