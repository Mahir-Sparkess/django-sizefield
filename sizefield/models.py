from django.db import models
from django.core import exceptions
from django.utils.translation import ugettext as _

from sizefield.utils import parse_size
from sizefield.widgets import FileSizeWidget


class FileSizeField(models.BigIntegerField):

    default_error_messages = {
        'invalid': _(u'Incorrect file size format.'),
    }

    def formfield(self, **kwargs):
        kwargs['widget'] = FileSizeWidget
        kwargs['error_messages'] = self.default_error_messages
        return super(FileSizeField, self).formfield(**kwargs)

    def to_python(self, value):
        if value is None:
            return None
        try:
            return parse_size(value)
        except ValueError:
            raise exceptions.ValidationError(self.error_messages['invalid'])

try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^sizefield\.models\.FileSizeField"])
except ImportError:
    pass
