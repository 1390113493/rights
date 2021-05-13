from django.urls import path
from .views import *

urlpatterns = [
    path('list', topic_list, name='topic_list'),
    path('detail', detail, name='detail'),
    path('newtopic', new_topic, name='new_topic'),
    path('addcomment', add_comment, name='add_comment'),
    path('search', search, name='search'),
    path('cate', cate, name='cate'),
    path('like', like_topic, name='like'),
    path('my', my, name='my'),
]