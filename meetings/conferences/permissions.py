from rest_framework import permissions

class CustomObjectPermissions(permissions.DjangoObjectPermissions):
    """
    Similar to `DjangoObjectPermissions`, but adding 'view' permissions.
    """
    perms_map = {
        'GET': ['%(app_label)s.public'],
        'OPTIONS': ['%(app_label)s.public'],
        'HEAD': ['%(app_label)s.public'],
        'POST': ['%(app_label)s.current_osf_user'],
        'PUT': ['%(app_label)s.conference_admin', '%(app_label)s.osf_admin'],
        'PATCH': ['%(app_label)s.conference_admin', '%(app_label)s.osf_admin'],
        'DELETE': ['%(app_label)s.conference_admin', '%(app_label)s.osf_admin'],
    }