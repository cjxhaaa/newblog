from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.get_blogs,name='index'),
    url(r'^detail/(?P<blog_id>\d+)/$',views.get_details,name='blog_get_detail'),
    # url(r'^detail/(?P<blog_id>\d+)/comment/$',views.comment,name='comment')
#     url(r'^article/(?P<pk>[0-9]+)$', views.PageView.as_view(),name='article_page'),
]