from django.conf.urls.defaults import patterns, url, include

urlpatterns = patterns('',
    url(r'^', include('autoapi.urls', namespace='autoapi')),
)
