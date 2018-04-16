from django.contrib.auth.models import User
from django.db import models


class AuditModel(models.Model):
    """
    Base model for others, providing creation, insertion, and update times
    """
    created_on = models.DateTimeField(auto_now_add=True)
    modified_on = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserProfile(AuditModel):
    """
    Store additional information on users
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20, null=True, default=None)


class Event(AuditModel):
    """
    General event model
    """
    name = models.CharField(max_length=255)
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    is_active = models.BooleanField(default=True)


class EventLocation(AuditModel):
    """
    Location of events
    """
    event = models.ForeignKey(Event, related_name='event_location', on_delete=models.CASCADE)
    street = models.CharField(max_length=100, null=True, blank=True)
    unit = models.CharField(max_length=16, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=2, null=True, blank=True)
    country = models.CharField(max_length=2, null=True, blank=True)
    zipcode = models.CharField(max_length=16, null=True, blank=True)


class RoleType(AuditModel):
    """
    Names of Roles users and events can have
    """
    name = models.CharField(max_length=255, unique=True)


class UserEventRole(AuditModel):
    """
    Relationships between Users and Events
    """
    role = models.ForeignKey(RoleType, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)


class EventDescription(AuditModel):
    """
    Addition information for Events
    """
    event = models.ForeignKey(Event, null=True, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)
    url = models.CharField(max_length=255, blank=True)
    image = models.ImageField(blank=True)
