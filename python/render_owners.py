import requests
from util import *


def list_authorized_users_and_teams():
    """
    Referance: https://api-docs.render.com/reference/get-owners
    This endpoint lists all users and teams that your API key has access to. This can be helpful for getting the correct ownerId to use for creating new resources, such as services.
    """

    url = f"{URL}/v1/owners"

    params = {
        'limit': '20',
        'name': '',
    }
    try:
        response = requests.get(url, params=params, headers=HEADERS)
        return response
    except Exception as e:
        print(e)
        return False


def retrieve_user_or_team(d_obj):
    """
    Referance: https://api-docs.render.com/reference/get-owner
    This endpoint gets information for a specific user or team that your API key has permission to access, based on ownerId.
    """

    url = f"{URL}/v1/owners/{d_obj['owner_id']}"


    try:
        response = requests.get(url, headers=HEADERS)
        return response
    except Exception as e:
        print(e)
        return False

