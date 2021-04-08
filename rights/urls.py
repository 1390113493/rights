from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings

urlpatterns = [
    path('', include(('index.urls', 'index'), namespace='index')),
    path('admin/', include(('admin.urls', 'admin'), namespace='admin')),
    path('common/', include(('common.urls', 'common'), namespace='common')),
    path('topic/', include(('topic.urls', 'topic'), namespace='topic')),
    path('user/', include(('user.urls', 'user'), namespace='user')),
    re_path('media/(?P<path>.*)', serve,
            {'document_root': settings.MEDIA_ROOT}, name='media')
]


handler404 = 'index.views.err404'
handler500 = 'index.views.err500'