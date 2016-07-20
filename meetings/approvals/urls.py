from django.conf.urls import url, include
from approvals import views

approval_list = views.ApprovalViewSet.as_view({
	'get': 'list', 
	'post':'create', 
})

approval_detail = views.ApprovalViewSet.as_view({
	'get': 'retrieve', 
    'patch':'partial_update'
})

urlpatterns = [
    url(r'^$', approval_list, name='list'),
    url(r'^(?P<pk>[-\w]+)/$', approval_detail, name='detail'),
]
