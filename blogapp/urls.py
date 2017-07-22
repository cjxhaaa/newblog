from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^detail/(\d+)/$',views.get_details,name='blog_get_detail'),
    url(r'^$', views.get_blogs),
#     url(r'^article/(?P<pk>[0-9]+)$', views.PageView.as_view(),name='article_page'),
]