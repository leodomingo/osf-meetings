from django.conf.urls import url
from files import views

files_list = views.FileViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
files_detail = views.FileViewSet.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    url(r'^$', files_list, name='list'),
    url(r'^(?P<pk>[-\w]+)/$', files_detail, name='detail'),
]
