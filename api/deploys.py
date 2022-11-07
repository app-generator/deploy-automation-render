# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import requests, json

from .common   import *
from .helpers  import *
from .owners   import *

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

def deploy_django(aRepo, aEntryPoint='core.wsgi:application'):
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
                    "buildCommand":"pip install --upgrade pip ; pip install -r requirements.txt ; python manage.py migrate",
                    "startCommand":f"gunicorn {aEntryPoint}"
                },
            },
            'type': 'web_service',
            'name': service_name,
            'ownerId': ownerId,
            'repo': aRepo,
        }

        response = requests.post(url, json=payload, headers=HEADERS)

        # HTTP 201 = Resource Created
        if 201 != response.status_code:
            raise Exception( response.text )

        response_json = json.loads( response.text )

        if DEBUG:
            print( ' > RESPONSE ' + str( response_json ) )        

        deploy_id  = response_json["deployId"]
        deploy_url = response_json["service"]["serviceDetails"]["url"]
        
        #if DEBUG:
        print(" > Deploy ID ["+deploy_id+"] -> " + deploy_url)

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

        # Process AppSeed Specific 
        if 'github.com/app-generator' in aRepo:
            aEntryPoint = "run:app"    

        payload = {
            'autoDeploy': 'yes',
            'envVars': [
                {
                    "key"   : "DEBUG",
                    "value" : "True"
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
            'name': service_name,
            'ownerId': ownerId,
            'repo': aRepo,
        }
            
        response = requests.post(url, json=payload, headers=HEADERS)

        # HTTP 201 = Resource Created
        if 201 != response.status_code:
            raise Exception( response.text )

        response_json = json.loads( response.text )

        if DEBUG:
            print( ' > RESPONSE ' + str( response_json ) )        

        deploy_id  = response_json["deployId"]
        deploy_url = response_json["service"]["serviceDetails"]["url"]
        
        #if DEBUG:
        print(" > Deploy ID ["+deploy_id+"] -> " + deploy_url)

        return json.loads( response.text )

    except Exception as e:
        print(e)
        return None 

def deploy_nodejs(aRepo, aEntryPoint='app.js', aNodeVer=NODE_16):
    """
    Referance: https://api-docs.render.com/reference/create-service
    """

    url     = f"{URL}/v1/services"

    try:

        ownerId      = get_owner()
        service_name = nameFromRepo( aRepo ) + '-' + randStr() 
        build_cmd    = 'npm i && npm run build'

        if not ownerId:
            raise Exception( 'Error getting owner' )

        if 'yarn' in RENDER_BUILDER:
            build_cmd = 'yarn && yarn build'

        payload = {
            'autoDeploy': 'yes',
            'envVars': [
                {
                    "key": "NODE_VERSION",
                    "value": aNodeVer
                }
            ],            
            'serviceDetails': {
                'env':  'node',
                "envSpecificDetails":{
                    "buildCommand":build_cmd,
                    "startCommand":f"node " + aEntryPoint
                },
            },
            'type': 'web_service',
            'name': service_name,
            'ownerId': ownerId,
            'repo': aRepo,
        }

        response = requests.post(url, json=payload, headers=HEADERS)

        # HTTP 201 = Resource Created
        if 201 != response.status_code:
            raise Exception( response.text )

        response_json = json.loads( response.text )

        if DEBUG:
            print( ' > RESPONSE ' + str( response_json ) )        

        deploy_id  = response_json["deployId"]
        deploy_url = response_json["service"]["serviceDetails"]["url"]
        
        #if DEBUG:
        print(" > Deploy ID ["+deploy_id+"] -> " + deploy_url)

        return json.loads( response.text )

    except Exception as e:
        print(e)
        return None 

def deploy_static(aRepo, aNodeVer=NODE_14):
    """
    Referance: https://api-docs.render.com/reference/create-service
    """

    url     = f"{URL}/v1/services"

    try:

        ownerId      = get_owner()
        service_name = nameFromRepo( aRepo ) + '-' + randStr()
        build_cmd    = 'npm i ; npm run build'

        if not ownerId:
            raise Exception( 'Error getting owner' )

        if 'yarn' in RENDER_BUILDER:
            build_cmd = 'yarn ; yarn build'

        payload = {
            'autoDeploy': 'yes',
            'envVars': [                {
                    "key": "NODE_VERSION",
                    "value": aNodeVer
                }                
            ],            
            'serviceDetails': {
                'publishPath': 'build',
                'pullRequestPreviewsEnabled': 'no',
                'buildCommand': build_cmd            
            },
            'type': 'static_site',
            'name': service_name,
            'ownerId': ownerId,
            'repo': aRepo,
        }

        response = requests.post(url, json=payload, headers=HEADERS)

        # HTTP 201 = Resource Created
        if 201 != response.status_code:
            raise Exception( response.text )

        response_json = json.loads( response.text )

        if DEBUG:
            print( ' > RESPONSE ' + str( response_json ) )        

        deploy_id  = response_json["deployId"]
        deploy_url = response_json["service"]["serviceDetails"]["url"]
        
        #if DEBUG:
        print(" > Deploy ID ["+deploy_id+"] -> " + deploy_url)

        return json.loads( response.text )

    except Exception as e:
        print(e)
        return None 

## APSEED Specific

def deploy_api_flask( aRepo='https://github.com/app-generator/api-server-flask' ):

    aEntryPoint = "run:app"

    return deploy_flask(aRepo, aEntryPoint)

def deploy_api_django( aRepo='https://github.com/app-generator/api-server-django' ):

    aEntryPoint = "core.wsgi:application"

    return deploy_django(aRepo, aEntryPoint)

def deploy_api_nodejs( aRepo='https://github.com/app-generator/api-server-nodejs' ):

    url = f"{URL}/v1/services"
             
    aEntryPoint = 'build/index.js' 
    aNodeVer    = NODE_16

    try:

        ownerId      = get_owner()
        service_name = nameFromRepo( aRepo ) + '-' + randStr() 
        build_cmd    = 'yarn && yarn typeorm migration:run && yarn build'

        if not ownerId:
            raise Exception( 'Error getting owner' )

        payload = {
            'autoDeploy': 'yes',
            'envVars': [
                {
                    "key": "NODE_VERSION",
                    "value": aNodeVer
                }
            ],            
            'serviceDetails': {
                'env':  'node',
                "envSpecificDetails":{
                    "buildCommand":build_cmd,
                    "startCommand":f"node " + aEntryPoint
                },
            },
            'type': 'web_service',
            'name': service_name,
            'ownerId': ownerId,
            'repo': aRepo,
        }

        response = requests.post(url, json=payload, headers=HEADERS)

        # HTTP 201 = Resource Created
        if 201 != response.status_code:
            raise Exception( response.text )

        response_json = json.loads( response.text )

        if DEBUG:
            print( ' > RESPONSE ' + str( response_json ) )        

        deploy_id  = response_json["deployId"]
        deploy_url = response_json["service"]["serviceDetails"]["url"]
        
        #if DEBUG:
        print(" > Deploy ID ["+deploy_id+"] -> " + deploy_url)

        return json.loads( response.text )

    except Exception as e:
        print(e)
        return None 
