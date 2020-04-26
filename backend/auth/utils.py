import jwt
import logging


def get_username_from_cookie(request, raise_error=True):
    """
    Helper method to extract the username from a JWT token. By default it will raise an error if it does not find one
    because the auth token is often required for all operations but can be changed for internal use to just
    return None
    """
    try:
        if request.COOKIES:
            token = request.COOKIES.get('auth_token')
            if token:
                try:
                    token_decoded = jwt.decode(token, 'secret', algorithms=['HS256'])
                except Exception as e:
                    logging.error('Unable to decode the JWT token {}. Please login again.'.format(token))
                    if raise_error:
                        raise e
                    else:
                        return None
                username = token_decoded.get('username', None)
            else:
                username = request.data.get('username', None)  # if not in the cookie, try it from the POST itself
        else:
            username = request.data.get('username', None)
        logging.info("Decoded Username from Cookie - {}".format(username))
        return username
    except Exception as e:
        logging.info(e)
        raise RuntimeError("Cookie Not Found. Invalid Headers.")


def get_usergroups_from_cookie(request, raise_error=True):
    """
    :return: list of user groups
    """
    try:
        if request.COOKIES:
            token = request.COOKIES.get('auth_token')
            if token:
                try:
                    token_decoded = jwt.decode(token, 'secret', algorithms=['HS256'])
                except Exception as e:
                    logging.error('Unable to decode the JWT token {}. Please login again.'.format(token))
                    if raise_error:
                        raise e
                    else:
                        return None
                user_groups = token_decoded.get('groups', [])
            else:
                user_groups = request.data.get('groups', [])
        else:
            user_groups = request.data.get('groups', [])
        logging.info("Decoded User-Groups from Cookie - {}".format(user_groups))
        return user_groups
    except Exception as e:
        logging.info(e)
        raise RuntimeError("Cookie Not Found. Invalid Headers.")

        

def get_user_data(user):
    """
    Method to get details of a user

    :param user: a representation of a user. this can be either the User object OR the username only. Note that
    the string representation of a User object is just the username so the ORM command below works.
    :return: dictionary containing details of the user
    """
    try:
        username_obj = User.objects.get(username=str(user))
    except Exception as e:
        logging.error("No user found for username {}".format(user))
        raise RuntimeError("No user for username {}. Terminating auth action now" .format(user))

    if username_obj is not None:
        userdata = {
            'username': str(user),
            'name': username_obj.first_name + ' ' + username_obj.last_name,
            'email': username_obj.email,
            'group': (AuthenticationController.get_user_group(username_obj))
        }
        return userdata
    logging.error("No User found matching the username: {}".format(str(user)))
    return None


def get_user_group(username_obj):
    """
    Method to get the groups that a user belong to

    :param username_obj: User model object
    :return: A list of groups that the user belongs to
    """
    group_list = list(username_obj.groups.values_list('name', flat=True))

    return group_list


def add_user_group(username):
    """
    Wrapper method to get the list of groups for a user
    :param username: username of user
    :return:  A list of groups that the user belongs to
    """
    username_obj = User.objects.get(username=str(username))
    group_list = AuthenticationController.get_user_group(username_obj)

    return group_list


def is_user_in_group(user, group_user_list):
    """
    Check if user in group_user_list

    :param user: Django User object
    :param group_user_list: group names
    :return: Boolean
    """
    try:
        group_list = list(user.groups.values_list('name', flat=True))
    except Exception:
        group_list = []
    for group in group_user_list:
        if group in group_list:
            return True
    logging.info("User does not belong to any of the following groups: {}".format(group_user_list))
    return False
