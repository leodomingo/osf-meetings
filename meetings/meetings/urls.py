from django.conf.urls import url, include
from api import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^meetings/$', views.MeetingList.as_view()),
    url(r'^meetings/(?P<pk>[0-9]+)/$', views.MeetingDetail),
    url(r'^nodes/$', views.NodeList),
    url(r'^nodes/(?P<pk>[0-9]+)/$', views.NodeDetail),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^admin/', admin.site.urls),
]

# urlpatterns = format_suffix_patterns(urlpatterns)