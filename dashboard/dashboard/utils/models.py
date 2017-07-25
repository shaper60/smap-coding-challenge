from django.db import models
from django.utils.translation import ugettext_lazy as _


class SoftDeleteBase(models.Model):
    deleted = models.DateTimeField(null=True, blank=True)

    class Meta:
        abstract = True

    def delete(self, *args, **kwargs):
        if not self.pk:
            raise IntegrityError(_('Object is not created.'))
        self.deleted = datetime.datetime.now()
        return super(SoftDeleteBase, self).save(*args, **kwargs)

    def data_ensure(self, *args, **kwargs):
        if not self.pk:
            raise IntegrityError(_('Object is not created.'))
        super(SoftDeleteBase, self).delete(*args, **kwargs)