# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import requests, json

from .common   import *
from .helpers  import *
from .owners   import *

def list_services():
    """
    Referance: https://api-docs.render.com/reference/get-services
    This endpoint lists all services that are owned by your Render user and any teams you're a part of.
    """

    url = f"{URL}/v1/services"

    try:
        response = requests.get(url, headers=HEADERS)

        if 200 != response.status_code:
            raise Exception( response.text )

        if DEBUG:
            print( response.text ) 

        return json.loads( response.text )

    except Exception as e:
        print(e)
        return None

def deploy_flask(aRepo, aEntryPoint='app:app'):
    """
    Referance: https://api-docs.render.com/reference/create-service
    """

    url     = f"{URL}/v1/services"

    try:

        ownerId      = get_owner()
        service_name = nameFromRepo( aRepo ) + '-' + randStr() 

        if not ownerId:
            raise Exception( 'Error getting owner' )

        payload = {
            'autoDeploy': 'yes',
            'envVars': [
                {
                    "key": "DEBUG",
                    "value": "True"
                }
            ],            
            'serviceDetails': {
                'env':  'python',
                "envSpecificDetails":{
                    "buildCommand":"pip install --upgrade pip ; pip install -r requirements.txt",
                    "startCommand":f"gunicorn {aEntryPoint}"
                },
            },
            'type': 'web_service',
            'environment':  'python',
            'name': service_name,
            'ownerId': ownerId,
            'repo': aRepo,
        }

        response = requests.post(url, json=payload, headers=HEADERS)

        # HTTP 201 = Resource Created
        if 201 != response.status_code:
            raise Exception( response.text )

        response_json = json.loads( response.text )

        deploy_id  = response_json["deployId"]
        deploy_url = response_json["service"]["serviceDetails"]["url"]
        
        if DEBUG:

            print(" > Deploy ID ["+deploy_id+"] -> " + deploy_url)

        return json.loads( response.text )

    except Exception as e:
        print(e)
        return None 

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
