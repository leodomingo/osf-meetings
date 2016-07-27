from rest_framework import viewsets
from rest_framework import filters
from drf_haystack.serializers import HaystackSerializer
from drf_haystack.viewsets import HaystackViewSet
from conferences.models import Conference
from .search_indexes import ConferenceIndex
from conferences.serializers import ConferenceSerializer
from conferences.permissions import ConferencePermissions
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class ConferenceViewSet(viewsets.ModelViewSet):
    resource_name = 'conferences'
    queryset = Conference.objects.all()
    serializer_class = ConferenceSerializer
    filter_backends = (filters.SearchFilter, filters.DjangoObjectPermissionsFilter,)
    permission_classes = (ConferencePermissions, )
    search_fields = ('title', 'description')

    @method_decorator(login_required)
    def create(self, request, *args, **kwargs):
        return super(ConferenceViewSet, self).create(request, args, kwargs)

    def perform_create(self, serializer):
        serializer.save(admin=serializer.context['request'].user)


class ConferenceSerializer(HaystackSerializer):

    class Meta:
        # The `index_classes` attribute is a list of which search indexes
        # we want to include in the search.
        index_classes = [ConferenceIndex]

        # The `fields` contains all the fields we want to include.
        # NOTE: Make sure you don't confuse these with model attributes. These
        # fields belong to the search index!
        fields = [
            "text", "created", "modified", "title", "city","state", "description"
        ]
        field_aliases = {
            "q": "title",
            "q": "description"
        }


class ConferenceSearchView(HaystackViewSet):

    # `index_models` is an optional list of which models you would like to include
    # in the search result. You might have several models indexed, and this provides
    # a way to filter out those of no interest for this particular view.
    # (Translates to `SearchQuerySet().models(*index_models)` behind the scenes.
    index_models = [Conference]

    serializer_class = ConferenceSerializer

