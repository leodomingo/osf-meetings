from django.conf.urls import url
from uploads import views

upload_list = views.UploadViewSet.as_view({
    'get': 'list',
    'post': 'create',
})

upload_detail = views.UploadViewSet.as_view({
    'get': 'retrieve',
})

urlpatterns = [
    url(r'^$', upload_list, name='list'),
    url(r'^(?P<pk>[-\w]+)/$', upload_detail, name='detail'),
]
