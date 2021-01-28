from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

occurrence_id_regex = RegexValidator(
    regex=r'Unillanos:MHNU-[A-Z]{1,2}:\d+',
    message=_('Invalid format')
)
