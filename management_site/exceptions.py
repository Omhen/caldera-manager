

class ManagerException(Exception):
    pass


class InvalidParameterException(ManagerException):

    def __init__(self, param_name, reason):
        message = 'The Parameter {} is not valid. {}'.format(param_name, reason)
        super(InvalidParameterException, self).__init__(message)