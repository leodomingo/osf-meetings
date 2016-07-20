from guardian.shortcuts import assign_perm, remove_perm
from rest_framework import permissions


class ApprovalPermissions(permissions.DjangoObjectPermissions):

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


def add_approval_permissions_to_submission_contributor(approval, submission_contributor):
    assign_perm("approvals.delete_approval", submission_contributor, approval)
    assign_perm("approvals.view_approval", submission_contributor, approval)


def remove_approval_permissions_to_submission_contributor(approval, submission_contributor):
    remove_perm("approvals.delete_approval", submission_contributor, approval)
    remove_perm("approvals.view_approval", submission_contributor, approval)


def add_approval_permissions_to_conference_admin(approval, conference_admin):
    assign_perm("approvals.change_approval", conference_admin, approval)
    assign_perm("approvals.delete_approval", conference_admin, approval)
    assign_perm("approvals.view_approval", conference_admin, approval)


def remove_approval_permissions_to_conference_admin(approval, conference_admin):
    remove_perm("approvals.change_approval", conference_admin, approval)
    remove_perm("approvals.delete_approval", conference_admin, approval)
    remove_perm("approvals.view_approval", conference_admin, approval)
