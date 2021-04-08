from django.urls import path
from .views import *

urlpatterns = [
    path('gettopiclist1', getTopicList1, name='gettopiclist1'),
    path('gettopiclist2', getTopicList2, name='gettopiclist2'),
    path('gettopicdetail', getTopicDetail, name='gettopicdetail'),
    path('deltopic', delTopic, name='deltopic'),
    path('checktopic', checkTopic, name='checktopic'),
    path('categorylist', categoryList, name='categorylist'),
    path('editcategory', editCategory, name='editcategory'),
    path('addcategory', addCategory, name='addcategory'),
    path('delcategory', delCategory, name='delcategory'),
    path('userlist', userList, name='userlist'),
    path('userdetail', userDetail, name='userdetail'),
    path('appset', appSet, name='appset'),
]