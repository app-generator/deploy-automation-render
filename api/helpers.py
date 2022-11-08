# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import requests, random, string, json

from .common   import *

def randStr( aLen=3 ):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=aLen )).lower()

def nameFromRepo( aRepoURL ):

    if not aRepoURL:
        return aRepoURL

    aRepoURL = aRepoURL.replace('.git', '')
    return aRepoURL.split('/')[-1]

def pp_json( aJson ):

    try: 

        return json.dumps(aJson, indent=2)
    
    except:
        return ''

def github_repo_meta( aRepo ):

    deployer_json = None  # root of the REPO
    ui_json       = None  # UI compatib matrix

    try: 

        deployer_json_url = aRepo.replace('github.com', 'raw.github.com') + '/main/deployer.json'
        r = requests.get(deployer_json_url, allow_redirects=True)
        deployer_json_str = r.content.decode('utf8').replace("'", '"')

        if '404' in deployer_json_str:
            raise Exception('Repo Metadata not found (deployer.json in ROOT)')

        deployer_json = json.loads( deployer_json_str )

        inner_dirs = deployer_json['dirs'].replace(' ', '')

        dir_api = None 
        dir_ui  = None 

        for k in inner_dirs.split(','):
            if '-api' in k:
               dir_api = k
            if '-ui' in k:
               dir_ui = k

        # print('> API [' +dir_api+ '] -> [' + dir_ui + ']')

        ui_json_url = deployer_json_url.replace( 'deployer.json', dir_ui + '/package.json')
        r = requests.get(ui_json_url, allow_redirects=True)
        ui_json_str = r.content.decode('utf8').replace("'", '"')

        if '404' in ui_json_str:
            raise Exception('UI package.json not found')

        ui_json = json.loads( ui_json_str )

        return True, deployer_json, dir_api, dir_ui, ui_json  

    except Exception as e:
        print( str( e ) )
        return False, None, None, None, None
