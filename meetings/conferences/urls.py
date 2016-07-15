from django.conf.urls import url, include
from conferences import views

urlpatterns = [
    url(r'^$', views.ConferenceList.as_view({'get': 'list', 'post':'create'}), name='list'),
    url(r'^(?P<pk>[-\w]+)/$', views.ConferenceDetail.as_view(), name='detail'),
    url(r'^(?P<conference_id>[-\w]+)/submissions/', include('submissions.urls',
        namespace='submissions')),
    url(regex=r'^(?P<pk>[-\w]+)/relationships/(?P<related_field>[^/.]+)$',
        view=views.ConferenceRelationshipView.as_view(),
        name='conference-relationships'
    )
]
