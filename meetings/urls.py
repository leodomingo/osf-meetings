from django.conf.urls import url, include
from rest_framework import routers
from api import views
from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'nodes', views.NodeViewSet)
router.register(r'submission-evals', views.SubmissionEvalViewSet)
router.register(r'meetings', views.MeetingViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^v2/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', admin.site.urls),

]