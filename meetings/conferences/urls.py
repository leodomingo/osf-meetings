from django.conf.urls import url
from conferences import views

urlpatterns = [
    url(r'^$', views.ConferenceList.as_view(), name='list'),
    url(r'^(?P<pk>[0-9]+)/$', views.ConferenceDetail.as_view(), name='detail'),
]
