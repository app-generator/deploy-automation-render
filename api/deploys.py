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

def deploy_django(aRepo, aEntryPoint=ENTRY_POINT_DJANGO, aRootPath=None):
    """
    Referance: https://api-docs.render.com/reference/create-service
    """

    url     = f"{URL}/v1/services"

    try:

        ownerId      = get_owner()
        service_name = nameFromRepo( aRepo ) + '-' + randStr() 

        build_cmd    = 'pip install --upgrade pip && pip install -r requirements.txt && python manage.py migrate'
        start_cmd    =  f"gunicorn {aEntryPoint}"

        if aRootPath:
            build_cmd    = 'cd ' + aRootPath + ' ; ' + build_cmd
            start_cmd    = 'cd ' + aRootPath + ' ; ' + start_cmd
            service_name = nameFromRepo( aRepo, True ) + '-' + aRootPath + '-' + randStr(3) 
        else:
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
                    "buildCommand": build_cmd,
                    "startCommand": start_cmd
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

        #if DEBUG:
        #    print( ' > RESPONSE ' + str( response_json ) )        

        deploy_id  = response_json["deployId"]
        deploy_url = response_json["service"]["serviceDetails"]["url"]
        
        #if DEBUG:
        print(" > Deploy ID ["+deploy_id+"] -> " + deploy_url)

        return response_json

    except Exception as e:
        print(e)
        return None 

def deploy_flask(aRepo, aEntryPoint=ENTRY_POINT_FLASK  , aRootPath=None):
    """
    Referance: https://api-docs.render.com/reference/create-service
    """

    url     = f"{URL}/v1/services"

    try:

        ownerId      = get_owner()
        service_name = nameFromRepo( aRepo ) + '-' + randStr() 

        build_cmd    = 'pip install --upgrade pip ; pip install -r requirements.txt'
        start_cmd    =  f"gunicorn {aEntryPoint}"

        if aRootPath:
            build_cmd    = 'cd ' + aRootPath + ' ; ' + build_cmd
            start_cmd    = 'cd ' + aRootPath + ' ; ' + start_cmd
            service_name = nameFromRepo( aRepo, True ) + '-' + aRootPath + '-' + randStr(3) 
        else:
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
                    "buildCommand": build_cmd,
                    "startCommand": start_cmd
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

        #if DEBUG:
        #    print( ' > RESPONSE ' + str( response_json ) )        

        deploy_id  = response_json["deployId"]
        deploy_url = response_json["service"]["serviceDetails"]["url"]
        
        #if DEBUG:
        print(" > Deploy ID ["+deploy_id+"] -> " + deploy_url)

        return json.loads( response.text )

    except Exception as e:
        print(e)
        return None 

def deploy_nodejs(aRepo, aEntryPoint=ENTRY_POINT_NODEJS, aNodeVer=NODE_16, aRootPath=None):
    """
    Referance: https://api-docs.render.com/reference/create-service
    """

    url     = f"{URL}/v1/services"

    try:

        ownerId      = get_owner()
        service_name = nameFromRepo( aRepo ) + '-' + randStr() 
        build_cmd    = 'npm i && npm run typeorm migration:run ; npm run build'
        start_cmd    = f"node " + aEntryPoint

        if 'yarn' in RENDER_BUILDER:
            build_cmd = 'yarn && yarn typeorm migration:run && yarn build'

        if aRootPath:
            build_cmd    = 'cd ' + aRootPath + ' ; ' + build_cmd
            start_cmd    = 'cd ' + aRootPath + ' ; ' + start_cmd
            service_name = nameFromRepo( aRepo, True ) + '-' + aRootPath + '-' + randStr(3) 
        else:
            service_name = nameFromRepo( aRepo ) + '-' + randStr()    

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
                    "buildCommand": build_cmd,
                    "startCommand": start_cmd
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

        #if DEBUG:
        #    print( ' > RESPONSE ' + str( response_json ) )        

        deploy_id  = response_json["deployId"]
        deploy_url = response_json["service"]["serviceDetails"]["url"]
        
        #if DEBUG:
        print(" > Deploy ID ["+deploy_id+"] -> " + deploy_url)

        return json.loads( response.text )

    except Exception as e:
        print(e)
        return None 

def deploy_static(aRepo, aNodeVer=NODE_16, aBuilder='yarn', aRootPath=None, aApiURL=None):
    """
    Referance: https://api-docs.render.com/reference/create-service
    """

    url     = f"{URL}/v1/services"

    try:

        ownerId      = get_owner()
        service_name = None
        build_cmd    = 'npm i ; npm run build'
        publish_path = 'build'

        if 'yarn' in aBuilder:
            build_cmd = 'yarn ; yarn build'

        if aRootPath:
            build_cmd    = 'cd ' + aRootPath + ' ; ' + build_cmd
            publish_path = aRootPath + '/build'
            service_name = nameFromRepo( aRepo, True ) + '-' + aRootPath
        else:
            service_name = nameFromRepo( aRepo ) + '-' + randStr()   

        if not ownerId:
            raise Exception( 'Error getting owner' )

        if not aApiURL:
            aApiURL = 'NA'

        payload = {
            'autoDeploy': 'yes',
            'envVars': [ 
                {
                    "key": "NODE_VERSION",
                    "value": aNodeVer
                },
                {
                    "key": "REACT_APP_BACKEND_SERVER",
                    "value": aApiURL
                }
            ],            
            'serviceDetails': {
                'publishPath': publish_path,
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

        #if DEBUG:
        #    print( ' > RESPONSE ' + str( response_json ) )        

        deploy_id  = response_json["deployId"]
        deploy_url = response_json["service"]["serviceDetails"]["url"]
        
        #if DEBUG:
        print(" > Deploy ID ["+deploy_id+"] -> " + deploy_url)

        return json.loads( response.text )

    except Exception as e:
        print(e)
        return None 

## APSEED Specific

def deploy_api_flask( aRepo='https://github.com/app-generator/api-server-flask', aRootPath=None ):

    aEntryPoint = ENTRY_POINT_FLASK

    return deploy_flask(aRepo, aEntryPoint, aRootPath)

def deploy_api_django( aRepo='https://github.com/app-generator/api-server-django', aRootPath=None ):

    aEntryPoint = ENTRY_POINT_DJANGO

    return deploy_django(aRepo, aEntryPoint, aRootPath)

def deploy_api_nodejs( aRepo='https://github.com/app-generator/api-server-nodejs', aRootPath=None ):

    url = f"{URL}/v1/services"
             
    aEntryPoint = 'build/index.js' 
    aNodeVer    = NODE_16

    try:

        ownerId      = get_owner()
        service_name = nameFromRepo( aRepo, True ) + '-' + aRootPath + '-' + randStr(3)  
        build_cmd    = 'yarn && yarn typeorm migration:run && yarn build'

        if aRootPath:
            build_cmd = 'cd ' + aRootPath + ' ; ' + build_cmd

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

        #if DEBUG:
        #    print( ' > RESPONSE ' + str( response_json ) )        

        deploy_id  = response_json["deployId"]
        deploy_url = response_json["service"]["serviceDetails"]["url"]
        
        #if DEBUG:
        print(" > Deploy ID ["+deploy_id+"] -> " + deploy_url)

        return json.loads( response.text )

    except Exception as e:
        print(e)
        return None 

def deploy_fullstack(aRepo):

    url     = f"{URL}/v1/services"

    try:

        ownerId = get_owner()

        # Get metadata from repo

        retVal, deployer_json, dir_api, dir_ui, ui_json = github_repo_meta( aRepo )

        if not retVal:
            raise Exception( 'Error getting metadata for REPO' )     
            return None 

        print(' FullStack > API [' + str(dir_api) + '] -> [' + str(dir_ui) + ']')

        api_url          = None 
        service_api_json = None 
        service_ui_json  = None

        # Deploy DJANGO
        if 'django' in dir_api:
            service_api_json = deploy_django(aRepo, ENTRY_POINT_DJANGO, dir_api)    

            if not service_api_json:
                raise Exception('Error deploying (DJANGO) API')

            api_url = service_api_json["service"]["serviceDetails"]["url"] + '/api/'

        # Deploy FLASK
        elif 'flask' in dir_api:
            service_api_json = deploy_flask(aRepo, ENTRY_POINT_FLASK, dir_api)    

            if not service_api_json:
                raise Exception('Error deploying (FLASK) API')

            api_url = service_api_json["service"]["serviceDetails"]["url"] + '/api/'

        # Deploy NODEJ
        elif 'nodejs' in dir_api:
            service_api_json = deploy_nodejs(aRepo, ENTRY_POINT_NODEJS, NODE_16, dir_api)    

            if not service_api_json:
                raise Exception('Error deploying (NODEJS) API')

            api_url = service_api_json["service"]["serviceDetails"]["url"] + '/api/'

        else:
            raise Exception('Error: Unsupported API: ' + dir_api)

        # Deploy UI 
        ui_nodejs_ver = NODE_16

        try:
            nodejs_all_vers = ui_json['build']['yarn']
            ui_nodejs_ver = nodejs_all_vers.split(',')[-1] 

            print( ' > UI, use NODE = ' + ui_nodejs_ver + ' from list=' + nodejs_all_vers)
        except:
            ui_nodejs_ver = NODE_16
            pass 

        service_ui_json = deploy_static(aRepo, ui_nodejs_ver, 'yarn', dir_ui, api_url)

        if not service_ui_json:
            raise Exception('Error deploying the UI')

        ui_url = service_ui_json["service"]["serviceDetails"]["url"]

    except Exception as e:
        print(e)
        return None 
