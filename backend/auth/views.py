import logging
from datetime import datetime, timedelta
import jwt
import time

from django.conf import settings
from django.contrib.auth import authenticate, login as django_login, logout as django_logout
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework.response import Response
from rest_framework.views import APIView

from .controllers import AuthenticationController
from .models import TokenManager
from .utils import get_username_from_cookie, get_usergroups_from_cookie



class Login(APIView):
    """
    Only a post method should be supported here to create a new token for a login.
    """
    def post(self, request):
        """
        Method to login a user.
        """
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            django_login(request, user)
            request.session.set_expiry(None)
            result = True
            all_groups = list(user.groups.values_list('name', flat=True))
            expires_at = datetime.now() + timedelta(days=1000000)
            
            payload = {
                'username': request.user.username,
                'first_name': request.user.first_name,
                'last_name': request.user.last_name,
                'email': request.user.email,
                'groups': all_groups,
                'result': result,
                'expires_at': time.mktime(expires_at.timetuple())
            }
            encoded_jwt = jwt.encode(payload, 'secret', algorithm='HS256')
            response = Response(payload)

            response.set_cookie("auth_token", encoded_jwt.decode('utf-8'), max_age=None,
                                expires=expires_at, domain=settings.DOMAIN)
            logging.info("Successfully logged in. Returning this user data: {}".format(payload))

            end_date = timezone.now() + timedelta(minutes=30)
            token_manager_obj, created = TokenManager.objects.get_or_create(token_value=encoded_jwt.decode('utf-8'),
                                                                            token_end_date=end_date,
                                                                            created_by=user.username,
                                                                            updated_by=user.username)
            token_manager_obj.save()
            return response
        else:
            raise RuntimeError("Invalid Username or Password. Unable to login")


class Logout(APIView):
    def post(self, request):
        """
        Method to logout a user.
        """
        data = {}
        try:
            username = request.data.get("username")

            if username is None:
                logging.error("Unable to fetch user from request. No user to logout")
                response = Response('Unable to fetch user from request. No user to logout')
                token = request.COOKIES.get('auth_token')
                token_manager_obj = TokenManager.objects.filter(token_value=token).first()
                token_manager_obj.delete()
                response.delete_cookie("auth_token")
                return response

            data = AuthenticationController.get_user_data(username)
            logging.info("Logging out User - {}" .format(data))
            django_logout(request)

            data['result'] = True
            response = Response(data)
            token = request.COOKIES.get('auth_token')
            if token is not None:
                token_manager_obj = TokenManager.objects.filter(token_value=token).first()
                token_manager_obj.delete()
                response.delete_cookie("auth_token")
            else:
                logging.warning("Auth Token Not Available.")

        except Exception as e:
            logging.error("Error in logging out. Error: {}".format(e))
            data['result'] = False
            response = Response(data)

        return response


class UserView(APIView):
    def dispatch(self, request, *args, **kwargs):
        self.username = get_username_from_cookie(request)
        self.user_groups = get_usergroups_from_cookie(request)

        if not self.username:
            raise RuntimeError("Unable to fetch user from request.")

        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        data = AuthenticationController.get_user_data(self.username)
        logging.info("Got User Data - {}".format(data))
        return Response(data)

    def post(self, request):
        """
        Method to update user profile.
        """
        password = request.data.get('current', None)
        if password is not None:
            try:
                logged_user_obj = authenticate(request, username=self.username, password=password)
                new_pwd = request.data.get('newPW')
                if new_pwd is not None:
                    if new_pwd is not '':
                        try:
                            logged_user_obj.set_password(new_pwd)
                            logged_user_obj.save()
                        except Exception as e:
                            raise RuntimeError('Can not set new password. Current password is invalid')
                    else:
                        raise RuntimeError('Can not set new password. New password is blank')
                else:
                    raise RuntimeError('Can not set new password. New password is not provided.')
            except Exception as e:
                raise RuntimeError("Incorrect password!")

        else:
            try:
                logged_user_obj = User.objects.get(username=self.username)
                logged_user_obj.email = request.data.get('email', logged_user_obj.email)
                logged_user_obj.first_name = request.data.get('first_name', logged_user_obj.first_name)
                logged_user_obj.last_name = request.data.get('last_name', logged_user_obj.last_name)
                logged_user_obj.save()
            except Exception as e:
                raise RuntimeError("Can not update user profile!")

        data = AuthenticationController.get_user_data(self.username)
        logging.info("Got User Data - {}".format(data))
        return Response(data)

