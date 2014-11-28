# -*- encoding: utf-8 -*-
# This file is distributed under the same license as the Django package.
#
from __future__ import unicode_literals

# The *_FORMAT strings use the Django date format syntax,
# see http://docs.djangoproject.com/en/dev/ref/templates/builtins/#date
DATE_FORMAT = 'Y-m-d'
TIME_FORMAT = 'H:i:s'
DATETIME_FORMAT = 'Y-m-d H:i:s'
YEAR_MONTH_FORMAT = 'Y-m'
MONTH_DAY_FORMAT = 'm-d'
SHORT_DATE_FORMAT = 'Y-m-d'
SHORT_DATETIME_FORMAT = 'Y-m-d H:i:s'
FIRST_DAY_OF_WEEK = 1

# The *_INPUT_FORMATS strings use the Python strftime format syntax,
# see http://docs.python.org/library/datetime.html#strftime-strptime-behavior
DATE_INPUT_FORMATS = 'Y-m-d'
TIME_INPUT_FORMATS = 'H:i:s'
DATETIME_INPUT_FORMATS =  'Y-m-d H:i:s'
# DECIMAL_SEPARATOR = 
# THOUSAND_SEPARATOR = 
# NUMBER_GROUPING = 
