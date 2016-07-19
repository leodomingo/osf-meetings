from rest_framework import permissions
from guardian.shortcuts import assign_perm, remove_perm
from django.contrib.auth.models import User, Group
from osf_oauth2_adapter.apps import OsfOauth2AdapterConfig


class ConferencePermissions(permissions.DjangoObjectPermissions):

    """
    Similar to `DjangoObjectPermissions`, but adding 'view' permissions.
    """
    authenticated_users_only = False

    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': ['%(app_label)s.view_%(model_name)s'],
        'HEAD': ['%(app_label)s.view_%(model_name)s'],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }

    def has_permission(self, request, view):
        # ----------------------------------------------------------
        # OVERWRITING THIS METHOD FROM DRF
        #
        # This method gets called on list view and normally fails due to
        # the commented out line below.
        #
        # DjangoObjectPermissionsFilter ensures users can only see what they are supposed
        # to be able to see
        #
        # has_object_permission() in DjangoObjectPermissions ensures users can only
        # GET, POST, PATCH etc. on objects they have the required permissions for
        #
        # -----------------------------------------------------------
        # Workaround to ensure DjangoModelPermissions are not applied
        # to the root view when using DefaultRouter.
        if getattr(view, '_ignore_model_permissions', False):
            return True

        if hasattr(view, 'get_queryset'):
            queryset = view.get_queryset()
        else:
            queryset = getattr(view, 'queryset', None)

        assert queryset is not None, (
            'Cannot apply DjangoModelPermissions on a view that '
            'does not set `.queryset` or have a `.get_queryset()` method.'
        )

        perms = self.get_required_permissions(request.method, queryset.model)

        return (
            request.user and
            (request.user.is_authenticated()
             or not self.authenticated_users_only)
            # and request.user.has_perms(perms)
        )

def add_conference_permissions_to_public(conference):
    public = User.objects.get(username="AnonymousUser")
    assign_perm("conferences.view_conference", public, conference)

def remove_conference_permissions_from_public(conference):
    public = User.objects.get(username="AnonymousUser")
    remove_perm("conferences.view_conference", public, conference)


def add_conference_permissions_to_current_osf_user(conference):
    current_osf_users = Group.objects.get(
        name=OsfOauth2AdapterConfig.osf_users_group)
    assign_perm("conferences.view_conference", current_osf_users, conference)

def remove_conference_permissions_from_current_osf_user(conference):
    current_osf_users = Group.objects.get(
        name=OsfOauth2AdapterConfig.osf_users_group)
    remove_perm("conferences.view_conference", current_osf_users, conference)

def add_conference_permissions_to_conference_admin(conference, conference_admin):
    assign_perm(
        "conferences.change_conference", conference_admin, conference)
    assign_perm(
        "conferences.delete_conference", conference_admin, conference)
    assign_perm(
        "conferences.view_conference", conference_admin, conference)

def remove_conference_permissions_from_conference_admin(conference, conference_admin):
    remove_perm(
        "conferences.change_conference", conference_admin, conference)
    remove_perm(
        "conferences.delete_conference", conference_admin, conference)
    remove_perm(
        "conferences.view_conference", conference_admin, conference)
