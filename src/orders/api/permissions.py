from rest_framework.permissions import BasePermission
from django.utils.timezone import now
from datetime import timedelta, datetime

class OrderPermission(BasePermission):
    """
    Allows access only to authenticated users at 8AM to 7PM
    """
    def has_permission(self, request, view):
        currentـtime = now() + timedelta(hours=4, minutes=30)
        if  8 < currentـtime.hour < 19:
            return bool(request.user and request.user.is_authenticated)
        return False
