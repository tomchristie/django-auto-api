from django.db.models import get_model, get_models
from django.http import HttpResponse
from django.core.urlresolvers import reverse as _reverse
from serializers import Serializer, ModelSerializer, Field, RelatedField


mime_types = {
    'json': 'application/json',
    'xml': 'application/xml',
    'yaml': 'application/yaml',
    'csv': 'text/csv',
    'html': 'text/html'
}


def reverse(viewname, kwargs=None, request=None, format=None):
    """
    Like the regular 'reverse' function, but returns fully qualified urls,
    and takes an additional 'format' argument.
    """
    if format:
        kwargs['format'] = format
    url = _reverse(viewname, kwargs=kwargs)
    return request.build_absolute_uri(url)


def url_for_object(obj, request, format):
    """
    Return the canonical URL for a given model instance.
    Use the request to form an absolute URL, rather than a relative one,
    and use a format suffix (eg '.json') if one is provided.
    """
    app_name = obj._meta.app_label
    model_name = obj._meta.object_name.lower()
    kwargs = {'app_name': app_name, 'model': model_name, 'pk': obj.pk}
    return reverse('autoapi:instance', kwargs=kwargs,
                   request=request, format=format)


def get_api_root(request, format):
    """
    Return a dict of `model label` -> `url`.
    """
    ret = {}
    for model in get_models():
        app_name = model._meta.app_label
        model_name = model._meta.object_name.lower()
        kwargs = {'app_name': app_name, 'model': model_name}
        url = reverse('autoapi:list', kwargs=kwargs,
                      request=request, format=format)
        ret[app_name + '.' + model_name] = url
    return ret


class URLField(Field):
    def convert_field(self, obj, field_name):
        request = self.root.kwargs['request']
        format = self.root.kwargs['format']
        return url_for_object(obj, request, format)


class URLRelatedField(RelatedField):
    def convert(self, obj):
        request = self.root.kwargs['request']
        format = self.root.kwargs['format']
        return url_for_object(obj, request, format)


class APISerializer(ModelSerializer):
    url = URLField()

    class Meta:
        include_default_fields = True
        model_field_types = ('fields', 'many_to_many')
        depth = 0
        related_field = URLRelatedField


def root(request, format=None):
    root = get_api_root(request, format)
    format = format or 'html'
    content = Serializer().serialize(root, format)
    return HttpResponse(content, mime_types[format])


def list(request, app_name, model, format=None):
    serializer = APISerializer(request=request, format=format)
    queryset = get_model(app_name, model)._default_manager.all()
    format = format or 'html'
    content = serializer.serialize(queryset, format)
    return HttpResponse(content, mime_types[format])


def instance(request, app_name, model, pk, format=None):
    serializer = APISerializer(request=request, format=format)
    instance = get_model(app_name, model)._default_manager.get(pk=pk)
    format = format or 'html'
    content = serializer.serialize(instance, format)
    return HttpResponse(content, mime_types[format])
