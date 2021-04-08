from django.urls import path
from .views import *

urlpatterns = [
    path('list', topiclist, name='topiclist'),
    path('detail', detail, name='detail'),
    path('newtopic', newtopic, name='newtopic'),
    path('addcomment', addcomment, name='addcomment'),
    path('search', search, name='search'),
    path('cate', cate, name='cate'),
]