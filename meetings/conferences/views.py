from rest_framework import viewsets
from rest_framework import filters
from conferences.models import Conference
from conferences.serializers import ConferenceSerializer
from conferences.permissions import ConferencePermissions
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class ConferenceViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing conferences. ConferenceViewSet has two endpoints: 
    `/conferences` and `/conferences/{conference_id}`.

    ###Attributes
            
        name                type          description
        =======================================================================================================
        id                  string        Unique identifier used to refer to specific conference
        created             dateTime      Time when item was created
        modified            dateTime      Time when last modified
        title               string        Title of conference
        site                URL           URL link to conference website
        city                string        Conference location
        state               string        Conference location
        country             string        Conference location
        event_start         dateTime      Start date/time of conference
        event_end           dateTime      End date/time of conference
        submission_start    dateTime      Date/time conference starts allowing submissions
        submission_end      dateTime      Date/time conference stops allowing submissions
        logo                URL           URL link to conference image
        description         string        Description of conference
        admin               string        ID of user who created conference


    ###Create

        Method:        POST
        URL:           /conferences
        Query Params:  <none> TODO: Make sure these are none
        Body (JSONAPI): {  
            // mandatory
            "title":             string   TOOD: Find out if I need the types again?
            "city":              string
            "state":             string
            "country":           string
            "event-start":       dateTime
            "event-end":         dateTime
            "submission-start":  dateTime
            "submission-end":    dateTime
            // optional
            "description":       string
            "site":              URL
            "logo":              URL
        }
        Success: 200 OK

    ###Get Conference List

        Method:  GET
        URL:     /conferences
        Params:  none
        Success: 200 OK

    ###Get Conference

        Method:   GET
        URL:      /conferences/{conference_id}
        Params:   none
        Success:  200 OK

    ###Delete

        Method:        DELETE
        URL:           /conferences/{conference_id}
        Query Params:  <none>
        Success:       204 No Content

    ###Edit

        Method:   PATCH
        URL:      /conferences/{conference_id}
        TODO


    """
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
