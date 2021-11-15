import re
from calendar import isleap
from datetime import datetime

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

# regex = '^((((19|20)(([02468][048])|([13579][26]))-02-29(\/((0[1-9])|(1[' \
#         '0-9])|(2[0-9])|30|31))?))|((20[0-9][0-9])|(19[0-9][0-9]))-((((0' \
#         '[1-9])|(1[0-2]))-((0[1-9])|(1[0-9])|(2[0-8]))(\/((0[1-9])|(1[0-' \
#         '9])|(2[0-9])|30|31))?)|((((0[13578])|(1[02]))-31(\/((0[1-9])|(1' \
#         '[0-9])|(2[0-9])|30|31))?)|(((0[13-9])|(1[0-2]))-(29|30)(\/((0[1' \
#         '-9])|(1[0-9])|(2[0-9])|30|31))?))))(\/((((19|20)(([02468][048])' \
#         '|([13579][26]))-02-29))|((20[0-9][0-9])|(19[0-9][0-9]))-((((0[1' \
#         '-9])|(1[0-2]))-((0[1-9])|(1[0-9])|(2[0-8])))|((((0[13578])|(1[0' \
#         '2]))-31)|(((0[13-9])|(1[0-2]))-(29|30))))))?$'

occurrence_id_regex = RegexValidator(
    regex=r'(Unillanos|892000757-3):MHNU-[A-Z]{1,2}:\d{3,}',
    message=_('Invalid format')
)

catalog_number_regex = RegexValidator(
    regex='MHNU-[A-Z]{1,2}[ -]\d{3,}'
)


def validate_date(value):
    """
    Example test values that raise an error
    2020-02-29/29
    2021-02-27/26
    2021-02-27/2021-02-27
    2021-02-27/2021-02-20
    2022
    2021-03
    """

    regex = (
        '^(((20(([02468][048])|([13579][26]))-02-29(\/((0[1-9])|(1[0-9])'
        '|(2[0-9])|30|31))?))|(20[0-9]{2}(-(0[1-9]|1[0-2]))?)|(20[0-9][0'
        '-9])-((((0[1-9])|(1[0-2]))-((0[1-9])|(1[0-9])|(2[0-8]))(\/((0[1'
        '-9])|(1[0-9])|(2[0-9])|30|31))?)|((((0[13578])|(1[02]))-31(\/(('
        '0[1-9])|(1[0-9])|(2[0-9])|30|31))?)|(((0[13-9])|(1[0-2]))-(29|3'
        '0)(\/((0[1-9])|(1[0-9])|(2[0-9])|30|31))?))))(\/(((20(([02468]['
        '048])|([13579][26]))-02-29))|(20[0-9][0-9])-((((0[1-9])|(1[0-2]'
        '))-((0[1-9])|(1[0-9])|(2[0-8])))|((((0[13578])|(1[02]))-31)|((('
        '0[13-9])|(1[0-2]))-(29|30))))))?$'
    )

    match = re.search(regex, value)
    if not match:
        raise ValidationError(
            _('Invalid date or date format, must be: YYYY-MM-DD, YYYY-MM-DD/DD'
              ', YYYY-MM-DD/YYYY-MM-DD, YYYY or YYYY-MM')
        )

    range_error = False
    future_date_error = False
    now = datetime.now().date()

    if len(value) > 7:
        date_values = value.split('/')
        date = datetime.strptime(date_values[0], '%Y-%m-%d').date()
        # 2021-02-24/26 or 2021-02-24/2021-02-27
        if date and len(date_values) == 2:
            # 2021-02-24/26
            if len(date_values[1]) == 2:
                day = int(date_values[1])
                # 2020-02-29/29 or 2021-02-27/26 or 2021-02-29/31
                if date.day == day or date.day > day or isleap(
                        date.year) and date.month == 2 and day > 29:
                    range_error = True
                # if current date is (2021-01-30) and value is 2021-01-29/31
                elif date > now or datetime(date.year, date.month,
                                            day).date() > now:
                    future_date_error = True
            # 2021-02-24/2021-02-27
            elif len(date_values[1]) == 10:
                date_1 = datetime.strptime(date_values[0], '%Y-%m-%d').date()
                date_2 = datetime.strptime(date_values[1], '%Y-%m-%d').date()
                if date_1.year == date_2.year and \
                        date_1.month == date_2.month or date_1 > date_2:
                    range_error = True
                elif date_1 > now or date_2 > now:
                    future_date_error = True
        else:
            # if current date is (2021-01-30) and date is 2021-01-31
            if date > now:
                future_date_error = True
    else:
        date_values = value.split('-')
        if len(date_values) == 2:
            year, month = int(date_values[0]), int(date_values[1])
            if year > now.year or year == now.year and month > now.month:
                future_date_error = True
        else:
            year = int(date_values[0])
            if year > now.year:
                future_date_error = True

    if range_error:
        raise ValidationError(_('Invalid date range'))
    elif future_date_error:
        raise ValidationError(
            _('The date cannot be greater than the current date')
        )
