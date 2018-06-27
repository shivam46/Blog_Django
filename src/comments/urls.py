from django.conf.urls import url
from django.contrib import admin

from .views import (
	comment_thread,
	comment_delete,
	)

app_name="comments"

urlpatterns = [
    url(r'^(?P<id>\d+)/$', comment_thread, name='thread'),            #Django Code Review #3 on joincfe.com/youtube/
    url(r'^(?P<id>\d+)/delete/$', comment_delete,name='delete'),
    #url(r'^posts/$', "<appname>.views.<function_name>"),
]