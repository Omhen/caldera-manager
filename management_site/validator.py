from management_site.exceptions import InvalidParameterException


def is_int(name, value):
    try:
        int(value)
    except:
        raise InvalidParameterException(name, 'not an int')

def is_empty(value):
    if not isinstance(value, basestring) and not isinstance(value, list) and not isinstance(value, dict):
        return False
    if not value or len(value) == 0:
        return True
    return False