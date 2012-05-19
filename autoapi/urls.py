from django.conf.urls.defaults import patterns, url
from autoapi import views


def get_format_urlpatterns(urlpatterns):
    """
    Supplement existing urlpatterns with corrosponding patterns that also
    include a '.format' suffix.  Retains urlpattern ordering.
    """
    ret = []
    for urlpattern in urlpatterns:
        # Form our complementing '.format' urlpattern
        regex = urlpattern.regex.pattern.rstrip('$') + '.(?P<format>[a-z]+)$'
        view = urlpattern._callback or urlpattern._callback_str
        kwargs = urlpattern.default_args
        name = urlpattern.name
        # Add in both the existing and the new urlpattern
        ret.append(urlpattern)
        ret.append(url(regex, view, kwargs, name))
    return ret


urlpatterns = patterns('',
    url(regex=r'^$',
        view=views.root),
    url(regex=r'^(?P<app_name>[a-z]+)\.(?P<model>[a-z]+)$',
        view=views.list,
        name='list'),
    url(regex=r'^(?P<app_name>[a-z]+)\.(?P<model>[a-z]+)/(?P<pk>\d+)$',
        view=views.instance,
        name='instance'),
)

urlpatterns = get_format_urlpatterns(urlpatterns)
