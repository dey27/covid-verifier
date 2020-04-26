import traceback, logging

from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException


def custom_exception_handler(exc, context=None):
    """
    Class to wrap any unexpected non DRF exception into custom Unexpected Exception code
    REST_FRAMEWORK = {
        'EXCEPTION_HANDLER': 'utility.exceptionHandlers.custom_exception_handler.custom_exception_handler',
    }

    :param exc: Exception object
    :param context: Context object
    :return: None
    """

    if not isinstance(exc, APIException):
        s = ""
        for msg in exc.args:
            s += str(msg)
        exc = UnexpectedError(detail=s)
    tb = traceback.format_exc()
    logging.error("Custom exception handler caught the following error: {}. Traceback: {}"
        .format(exc.detail, tb))
    response = exception_handler(exc, context)

    return response


class UnexpectedError(APIException):
    """
    Class for UnexpectedError Exception.
    Exception to be raised unsure about the exact cause of failure. Ex: RunTimeError
    """
    status_code = 500
    default_detail = 'Unexpected Error occurred'
    default_code = 'unexpected_error'


class CustomError(APIException):
    """
    Usage - raise CustomError()
    """
    status_code = 500
    default_detail = 'Custom message'

