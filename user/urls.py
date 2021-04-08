from django.urls import path
from .views import *

urlpatterns = [
    path('login', login, name='login'),
    path('logout', logout, name='logout'),
    path('getinfo', getInfo, name='getinfo'),
    path('setinfo', setInfo, name='setinfo'),
    path('editinfo', editinfo, name='editinfo'),
    path('auth', auth, name='auth'),
]