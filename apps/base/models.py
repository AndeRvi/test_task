import uuid
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class BaseModel(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    created_at = models.DateTimeField(_("Created at"), auto_now_add=True,
                                      null=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True,
                                      null=True)

    @classmethod
    def get_admin_list_url(cls):
        return reverse(
            f'admin:{cls._meta.app_label}_{cls._meta.model_name}_changelist'
        )

    def get_admin_edit_url(self):
        return reverse(
            f'admin:{self._meta.app_label}_{self._meta.model_name}_change',
            args=(self.pk,)
        )

    class Meta(object):
        abstract = True
        ordering = ['-created_at']
