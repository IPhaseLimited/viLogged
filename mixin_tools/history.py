from django.db import models
from uuidfield import UUIDField


class HistoryFieldsMixin(models.Model):
    '''
    Adds common history fields to a model. changed_by field you need to populate yourself.
    Usage: 
    from ehealth_tools.django_tools.mixins import HistoryFieldsMixin
    class Area(HistoryFieldsMixin, models.Model):
        pass
    '''
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey('auth.User', null=True, blank=True,)
    uuid = UUIDField(auto_created=True, unique=True)

    # Used by django-simple-history
    @property
    def _history_user(self):
        return self.created_by

    @_history_user.setter
    def _history_user(self, value):
        self.created_by = value
    # END: Used by django-simple-history

    class Meta:
        abstract = True
