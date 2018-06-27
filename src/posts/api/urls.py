from django.conf.urls import url
from django.contrib import admin

from .views import (
	PostCreateAPIView,
	PostDeleteAPIView,
	PostDetailAPIView,
	PostListAPIView,
	PostUpdateAPIView
	

	)

app_name="posts"

urlpatterns = [
	url(r'^$', PostListAPIView.as_view(), name='list'),
    url(r'^create/$', PostCreateAPIView.as_view(),name='create'),
	url(r'^(?P<slug>[\w-]+)/$', PostDetailAPIView.as_view(), name='detail'),
   #url(r'^(?P<slug>[\w-]+)/$', post_detail, name='detail'), #Django Code Review #3 on joincfe.com/youtube/
	url(r'^(?P<slug>[\w-]+)/edit/$', PostUpdateAPIView.as_view(), name='update'),
	url(r'^(?P<slug>[\w-]+)/delete/$',PostDeleteAPIView.as_view(),name='dalete'),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]
