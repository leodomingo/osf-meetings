from django.conf.urls import url, include
from api import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.contrib import admin

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^conferences/$', views.ConferenceList.as_view()),
    url(r'^conferences/(?P<pk>[0-9]+)/$', views.ConferenceDetail),
    url(r'^nodes/$', views.NodeList.as_view()),
    url(r'^nodes/(?P<pk>[0-9]+)/$', views.NodeDetail.as_view()),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^auth/', views.OsfAuthorizationUrl.as_view()),
    url(r'^login/', views.OsfAuthorizationCode.as_view()),
    url(r'^admin/', admin.site.urls),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
