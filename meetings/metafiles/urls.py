from django.conf.urls import url
from metafiles import views

metafiles_list = views.MetafileViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
metafiles_detail = views.MetafileViewSet.as_view({
    'get': 'retrieve',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    url(r'^$', metafiles_list, name='list'),
    url(r'^(?P<pk>[-\w]+)/$', metafiles_detail, name='detail'),
]
