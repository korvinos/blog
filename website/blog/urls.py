from django.conf.urls import url
from .views import test, index


urlpatterns = [
    url(r'^$', index),
    url(r'^tag/$', test),
    url(r'^post/(?P<post_id>[0-9]+)/$', test),
    url(r'^category/$', test),
    url(r'^last/$', test),
    url(r'^contact/$', test),
]
