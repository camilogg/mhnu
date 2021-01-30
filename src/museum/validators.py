from datetime import datetime

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

occurrence_id_regex = RegexValidator(
    regex=r'(Unillanos|892000757-3):MHNU-[A-Z]{1,2}:\d+',
    message=_('Invalid format')
)

date_regex = RegexValidator(
    regex='^((((19|20)(([02468][048])|([13579][26]))-02-29(\/((0[1-9])|(1[0-9]'
          ')|(2[0-9])|30|31))?))|((20[0-9][0-9])|(19[0-9][0-9]))-((((0[1-9])|('
          '1[0-2]))-((0[1-9])|(1[0-9])|(2[0-8]))(\/((0[1-9])|(1[0-9])|(2[0-9])'
          '|30|31))?)|((((0[13578])|(1[02]))-31(\/((0[1-9])|(1[0-9])|(2[0-9])|'
          '30|31))?)|(((0[13-9])|(1[0-2]))-(29|30)(\/((0[1-9])|(1[0-9])|(2[0-9'
          '])|30|31))?))))(\/((((19|20)(([02468][048])|([13579][26]))-02-29))|'
          '((20[0-9][0-9])|(19[0-9][0-9]))-((((0[1-9])|(1[0-2]))-((0[1-9])|(1['
          '0-9])|(2[0-8])))|((((0[13578])|(1[02]))-31)|(((0[13-9])|(1[0-2]))-('
          '29|30))))))?$',
    message=_('Invalid format, must be: YYYY-MM-DD, YYYY-MM-DD/DD or '
              'YYYY-MM-DD/YYYY-MM-DD')
)


def validate_date_range(value):
    """
    Example test values that raise an error
    '2020-02-29/29'
    '2021-02-27/26'
    '2021-02-27/2021-02-27'
    '2021-02-27/2021-02-20'
    """
    date_values = value.split('/')
    error = False

    try:
        date = datetime.strptime(date_values[0], '%Y-%m-%d')
    except ValueError:
        date = None

    if date and len(date_values) == 2:
        if len(date_values[1]) == 2:
            day = int(date_values[1])
            if date.day == day or date.day > day:
                error = True
        elif len(date_values[1]) == 10:
            date_1 = datetime.strptime(date_values[0], '%Y-%m-%d')
            date_2 = datetime.strptime(date_values[1], '%Y-%m-%d')
            if date_1 == date_2 or date_1 > date_2:
                error = True

    if not date or error:
        raise ValidationError(_('Invalid date range'))
