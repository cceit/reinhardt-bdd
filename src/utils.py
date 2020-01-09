import re
import unicodedata

import six
from django.utils.functional import keep_lazy
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe, SafeText


def snakify(value):
    """
    Converts to ASCII. Converts spaces to underscores. Removes characters that
    aren't alphanumerics, underscores, or hyphens. Converts to lowercase.
    Also strips leading and trailing whitespace.

    :param string value: unsanitized value

    :returns: snakified value

    Usage:
        .. code-block:: python
            :linenos:

            >>> snakify('polls-report May 1, 2016')
            u'polls_report_may_1_2016'

    """
    value = force_text(value)
    value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore')\
        .decode('ascii')
    value = re.sub('[^\w\s-]', '', value).strip().lower()
    return mark_safe(re.sub('[-\s]+', '_', value))


snakify = keep_lazy(snakify, six.text_type, SafeText)
