import requests
from util import *


def list_deploys(d_obj):
    """
    Referance: https://api-docs.render.com/reference/get-deploys
    """

    url = f"{URL}/v1/services/{d_obj['service_id']}"

    try:
        response = requests.patch(url, headers=HEADERS)
        return response
    except Exception as e:
        print(e)
        return False


def trigger_a_deploy():
    """
    Referance: https://api-docs.render.com/reference/create-deploy
    """

    url = f"{URL}/v1/services/{d_obj['service_id']}"

    payload = {
        "clearCache": "clear"
    }

    try:
        response = requests.patch(url, json=payload, headers=HEADERS)
        return response
    except Exception as e:
        print(e)
        return False