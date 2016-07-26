from django.conf.urls import url, include
from conferences import views

conference_list = views.ConferenceViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

conference_detail = views.ConferenceViewSet.as_view({
    'get': 'retrieve',
    'delete': 'destroy',
    'patch': 'partial_update'
})

conference_detail = views.ConferenceViewSet.as_view({
    'get': 'retrieve',
    'delete': 'destroy',
    'patch': 'partial_update'
})

urlpatterns = [
    url(r'^$', conference_list, name='list'),
    url(r'^(?P<pk>[-\w]+)/$', conference_detail, name='detail'),
    url(r'^(?P<conference_id>[-\w]+)/submissions/',
        include('submissions.urls', namespace='submissions')),
]
