from django.urls import path
from .views import *

urlpatterns = [
    path('upimg', upimg, name='upimg'),
    path('about', about, name='about'),

]