from django.conf import settings
from rest_framework import exceptions
from rest_framework import permissions


class CustomPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.POST["key"] != settings.SPARROW_API_KEY or request.POST["key"] == "":
            raise exceptions.AuthenticationFailed("Security key is not matched.")
        return True