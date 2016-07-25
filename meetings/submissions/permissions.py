from rest_framework import permissions
from guardian.shortcuts import assign_perm, remove_perm
from django.contrib.auth.models import User, Group
from osf_oauth2_adapter.apps import OsfOauth2AdapterConfig


class SubmissionPermissions(permissions.DjangoObjectPermissions):

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
        # the commented out line in the return statement below.
        #
        # DjangoObjectPermissionsFilter ensures users can only see what they are supposed
        # to be able to see
        #
        # has_object_permission() in DjangoObjectPermissions ensures users can only
        # GET, POST, PATCH etc. on objects they have the required permissions for
        # -----------------------------------------------------------
        # Workaround to ensure DjangoModelPermissions are not applied
        # to the root view when using DefaultRouter.

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

        return (
            request.user and
            (request.user.is_authenticated()
             or not self.authenticated_users_only)
            # and request.user.has_perms(perms)
        )


def add_approved_submission_permissions_to_public(submission):
    public = User.objects.get(username="AnonymousUser")
    assign_perm("submissions.view_submission", public, submission)


def remove_approved_submission_permissions_from_public(submission):
    public = User.objects.get(username="AnonymousUser")
    remove_perm("submissions.view_submission", public, submission)


def add_approved_submission_permissions_to_current_osf_user(submission):
    current_osf_users = Group.objects.get(name=OsfOauth2AdapterConfig.osf_users_group)
    assign_perm("submissions.view_submission", current_osf_users, submission)


def remove_approved_submission_permissions_from_current_osf_user(submission):
    current_osf_users = Group.objects.get(name=OsfOauth2AdapterConfig.osf_users_group)
    remove_perm("submissions.view_submission", current_osf_users, submission)


def add_submission_permissions_to_submission_contributor(submission, submission_contributor):
    assign_perm("submissions.change_submission", submission_contributor, submission)
    assign_perm("submissions.delete_submission", submission_contributor, submission)
    assign_perm("submissions.view_submission", submission_contributor, submission)


def remove_submission_permissions_from_submission_contributor(
        submission, submission_contributor):
    remove_perm("submissions.change_submission", submission_contributor, submission)
    remove_perm("submissions.delete_submission", submission_contributor, submission)
    remove_perm("submissions.view_submission", submission_contributor, submission)


def add_submission_permissions_to_conference_admin(submission, submission_contributor):
    assign_perm("submissions.change_submission", submission_contributor, submission)
    assign_perm("submissions.delete_submission", submission_contributor, submission)
    assign_perm("submissions.view_submission", submission_contributor, submission)


def remove_submission_permissions_from_conference_admin(submission, submission_contributor):
    remove_perm("submissions.change_submission", submission_contributor, submission)
    remove_perm("submissions.delete_submission", submission_contributor, submission)
    remove_perm("submissions.view_submission", submission_contributor, submission)
