# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os, sys

from api import *

ACTIONS = {
    'check'          : ['NA'],
    'all_owners'     : ['NA'],
    'owner'          : ['NA'],
    'all_services'   : ['NA'],
    'flask'          : ['NA'],
    'django'         : ['NA'],
    'nodejs'         : ['NA'],
    'static'         : ['NA'],
    'nodejs_api'     : ['NA'],
    'django_api'     : ['NA'],
    'flask_api'      : ['NA'],
    'fullstack'      : ['NA'],
}

def parse_input( sys_argv ):

    input_len  = len( sys_argv )
    input_argv = sys_argv

    COMMAND   = ''
    ARGUMENT  = None 
    ARGUMENT2 = None
    ARGUMENT3 = None 

    if 1 == input_len:
        print( 'Usage: deployer.py COMMAND Argument' )
        print( '  > COMMANDs: ' + str( ACTIONS.keys() ) )
        exit(0)

    COMMAND = input_argv[1].lower()

    if input_len > 2:
        ARGUMENT = input_argv[2].lower()

    if input_len > 3:
        ARGUMENT2 = input_argv[3].lower()        

    if input_len > 4:
        ARGUMENT3 = input_argv[4].lower()        

    if COMMAND not in ACTIONS.keys():

        print('ERR: Invalid command ['+COMMAND+']. Expected ' + str( ACTIONS.keys() ) )
        exit(1)

    if 'check' == COMMAND:

        if not RENDER_API_KEY:
            print(' > RENDER_API_KEY -> not found in environment' )
        else:
            ownerId = get_owner()

            if ownerId:
                print(' > Conn RENDER_API [OK], (default) ownerId=' + ownerId)
            else:
                print(' > Conn RENDER_API [ERR], (RENDER_API_KEY seems unusable)')        

        exit(1)

    if 'all_owners' == COMMAND:
        res = list_owners()
        exit(1)        

    if 'owner' == COMMAND:
        res = get_owner()
        exit(1)        

    if 'all_services' == COMMAND:
        res = list_services()
        exit(1)            

    if 'django' == COMMAND:

        REPO        = ARGUMENT 
        ENTRY_POINT = ARGUMENT2

        if not REPO:
            print('ERR: command ['+COMMAND+'] expects 2 inputs' )
            print(' > deployer ['+COMMAND+'] <REPO> <ENTRY_POINT>' )
            print(' > <REPO> = public repo to be deployed' )
            print(' > <ENTRY_POINT> = WSGI entry point, default="core.wsgi:application"' )
            exit(1)

        if not ENTRY_POINT:
            ENTRY_POINT = "core.wsgi:application"

        res = deploy_django(REPO, ENTRY_POINT)
        exit(1)  

    if 'flask' == COMMAND:

        REPO        = ARGUMENT 
        ENTRY_POINT = ARGUMENT2

        if not REPO:
            print('ERR: command ['+COMMAND+'] expects 2 inputs' )
            print(' > deployer ['+COMMAND+'] <REPO> <ENTRY_POINT>' )
            print(' > <REPO> = public repo to be deployed' )
            print(' > <ENTRY_POINT> = WSGI entry point, default="app:app"' )
            exit(1)

        if not ENTRY_POINT:
            ENTRY_POINT = "app:app"

        res = deploy_flask(REPO, ENTRY_POINT)
        exit(1)  

    if 'nodejs' == COMMAND:

        REPO        = ARGUMENT 
        ENTRY_POINT = ARGUMENT2
        NODE_VER    = ARGUMENT3

        if not REPO:
            print('ERR: command ['+COMMAND+'] expects 3 inputs' )
            print(' > deployer ['+COMMAND+'] <REPO> <ENTRY_POINT> <NODE_VER>' )
            print(' > <REPO> = public repo to be deployed' )
            print(' > <ENTRY_POINT> = APP entry point, default="app.js"' )            
            print(' > <NODE_VER> = Node Version, default='+NODE_16 )               
            exit(1)

        if not NODE_VER:
            NODE_VER = NODE_16
        else:

            if '12' in NODE_VER:
                NODE_VER = NODE_12
            elif '14' in NODE_VER:
                NODE_VER = NODE_14
            elif '16' in NODE_VER:
                NODE_VER = NODE_16
            elif '18' in NODE_VER:
                NODE_VER = NODE_18
            else:
                # Default to 16
                NODE_VER = NODE_16

        res = deploy_nodejs(REPO, ENTRY_POINT, NODE_VER)
        exit(1)  

    if 'static' == COMMAND:

        REPO     = ARGUMENT 
        NODE_VER = ARGUMENT2

        if not REPO:
            print('ERR: command ['+COMMAND+'] expects 2 inputs' )
            print(' > deployer ['+COMMAND+'] <REPO> <NODE_VER>' )
            print(' > <REPO> = public repo to be deployed' )
            print(' > <NODE_VER> = Node Version, default='+NODE_14 )            
            exit(1)

        if not NODE_VER:
            NODE_VER = NODE_14
        else:

            if '12' in NODE_VER:
                NODE_VER = NODE_12
            elif '14' in NODE_VER:
                NODE_VER = NODE_14
            elif '16' in NODE_VER:
                NODE_VER = NODE_16
            elif '18' in NODE_VER:
                NODE_VER = NODE_18
            else:
                # Default to 14
                NODE_VER = NODE_14

        res = deploy_static( REPO, NODE_VER )
        exit(1)          

    if 'nodejs_api' == COMMAND:

        REPO = ARGUMENT

        if REPO:
            res = deploy_api_nodejs( REPO )
        else:    
            res = deploy_api_nodejs( )

        exit(1) 

    if 'flask_api' == COMMAND:

        REPO = ARGUMENT

        if REPO:
            res = deploy_api_flask( REPO )
        else:    
            res = deploy_api_flask( ) 
        
        exit(1) 

    if 'django_api' == COMMAND:

        REPO = ARGUMENT

        if REPO:
            res = deploy_api_django( REPO )
        else:    
            res = deploy_api_django( ) 

        exit(1) 

    if 'fullstack' == COMMAND:

        REPO = ARGUMENT 

        if not REPO:
            print('ERR: command ['+COMMAND+'] expects 1 input' )
            print(' > deployer ['+COMMAND+'] <REPO>' )
            print(' > <REPO> = public repo to be deployed' )
            exit(1)

        res = deploy_fullstack( REPO )
        exit(1)          

# Entry point
if __name__ == "__main__": 
    parse_input( sys.argv )
