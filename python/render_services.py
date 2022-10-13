import requests
from util import *


def list_services():
    """
    Referance: https://api-docs.render.com/reference/get-services
    This endpoint lists all services that are owned by your Render user and any teams you're a part of.
    """

    url = f"{URL}/v1/services"

    params = {
        'limit': '20',
    }
    try:
        response = requests.get(url, params=params, headers=HEADERS)
        return response
    except Exception as e:
        print(e)
        return False


def create_service(d_obj):
    """
    Referance: https://api-docs.render.com/reference/create-service
    """

    url = f"{URL}/v1/services"

    payload = {
        'autoDeploy': 'yes',
        'serviceDetails': {
            'publishPath': 'public',
            'pullRequestPreviewsEnabled': 'no',
        },
        'type': 'static_site',
        'name': 'react-dash-board',
        'ownerId': '123456',
        'repo': 'https://github.com/app-generator/django-react-soft-dashboard',
        'branch': 'main',
    }

    try:
        response = requests.post(url, json=payload, headers=HEADERS)
        return response
    except Exception as e:
        print(e)
        return False



def retrieve_service(d_obj):
    """
    Referance: https://api-docs.render.com/reference/get-service
    """

    url = f"{URL}/v1/services/{d_obj['service_id']}"


    try:
        response = requests.get(url, headers=HEADERS)
        return response
    except Exception as e:
        print(e)
        return False



def update_service(d_obj):
    """
    Referance: https://api-docs.render.com/reference/update-service
    Update service allows you to update the configuration details of service, such as start commands and branches.
    Changes will not be deployed automatically. Instead you must call the deploy API to have changes pushed out to your service, irrespective of the autoDeploy option set on the service.
    """

    url = f"{URL}/v1/services/{d_obj['service_id']}"

    payload = {
        "autoDeploy": "yes",
        "branch": "main",
        "name": "react-dash-board"
    }

    try:
        response = requests.patch(url, json=payload, headers=HEADERS)
        return response
    except Exception as e:
        print(e)
        return False


def delete_service(d_obj):
    """
    Referance: https://api-docs.render.com/reference/delete-service
    """

    url = f"{URL}/v1/services/{d_obj['service_id']}"


    try:
        response = requests.delete(url, headers=HEADERS)
        return response
    except Exception as e:
        print(e)
        return False
