from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(),name='index'),
    url(r'^detail/(?P<blog_id>\d+)/$',views.BlogDetailView.as_view(),name='blog_get_detail'),
    url(r'^detail/(?P<blog_id>\d+)/comment/$',views.CommentView,name='comment'),
    url(r'^category/(?P<cate_id>\d+)/$',views.CategoryView.as_view(),name='category'),
    url(r'^archives/$', views.ArchivesView.as_view(),name='archives'),
    # url(r'^archives/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/$)',views.ArchivesView.as_view(),name='archives')
]