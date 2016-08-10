from django.conf.urls import url
from mail import views

urlpatterns = [
    url(r'^$', views.on_incoming_message, name='incoming_message'),
]
