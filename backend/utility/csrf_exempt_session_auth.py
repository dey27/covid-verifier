from rest_framework.authentication import SessionAuthentication


class CsrfExemptSessionAuthentication(SessionAuthentication):
    """
    Class to exempt CSRF Authentication on the application. This is used in settings.py by adding the below code.
    REST_FRAMEWORK = {
        'DEFAULT_AUTHENTICATION_CLASSES': (
            'authentication.csrf_exempt_session_authentication.CsrfExemptSessionAuthentication',
        )
    }
    """

    def enforce_csrf(self, request):
        """
        Empty method so CSRF auth is disabled
        """

        return  # nothing, so not to perform the csrf check
