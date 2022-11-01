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
    'deploy_flask'   : ['NA'],
}

def parse_input( sys_argv ):

    input_len  = len( sys_argv )
    input_argv = sys_argv

    COMMAND   = ''
    ARGUMENT  = None 
    ARGUMENT2 = None 

    if 1 == input_len:
        print( 'Usage: runner.py COMMAND Argument' )
        print( '  > COMMANDs: ' + str( ACTIONS.keys() ) )
        exit(0)

    COMMAND = input_argv[1].lower()

    if input_len > 2:
        ARGUMENT = input_argv[2].lower()

    if input_len > 3:
        ARGUMENT2 = input_argv[3].lower()        

    if COMMAND not in ACTIONS.keys():

        print('ERR: Invalid command ['+COMMAND+']. Expected ' + str( ACTIONS.keys() ) )
        exit(1)

    if 'check' == COMMAND:

        if not RENDER_API_KEY:
            print(' > RENDER_API_KEY -> not found in environment' )
        else:
            if DEBUG:
                print(' > RENDER_API_KEY -> ' + str( RENDER_API_KEY ) )
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

    if 'deploy_flask' == COMMAND:

        REPO        = ARGUMENT 
        ENTRY_POINT = ARGUMENT2

        if not REPO:
            print('ERR: command ['+COMMAND+'] expects 2 inputs' )
            print(' > runner create_service <REPO> <ENTRY_POINT>' )
            print(' > <REPO> = public repo to be deployed<ENTRY_POINT>' )
            print(' > <ENTRY_POINT> = WSGI entry point, default="app:app"' )
            exit(1)

        if not ENTRY_POINT:
            ENTRY_POINT = "app:app"

        res = deploy_flask(REPO, ENTRY_POINT)
        exit(1)  

# Entry point
if __name__ == "__main__": 
    parse_input( sys.argv )
