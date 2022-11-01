# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os, sys

from api import *

ACTIONS = {
    'check'      : ['NA'],
    'all_owners' : ['NA'],
    'owner'      : ['NA'],
}

def parse_input( sys_argv ):

    input_len  = len( sys_argv )
    input_argv = sys_argv

    COMMAND   = ''
    ARGUMENT  = None 

    if 1 == input_len:
        print( 'Usage: runner.py COMMAND Argument' )
        print( '  > COMMANDs: ' + str( ACTIONS.keys() ) )
        exit(0)

    COMMAND = input_argv[1].lower()

    if input_len > 2:
        ARGUMENT = input_argv[2].lower()

    if COMMAND not in ACTIONS.keys():

        print('ERR: Invalid command ['+COMMAND+']. Expected ' + str( ACTIONS.keys() ) )
        exit(1)

    if 'check' == COMMAND:
        if DEBUG:
            print(' > RENDER_API_KEY -> ' + str( RENDER_API_KEY ) )
        exit(1)

    if 'all_owners' == COMMAND:

        # list
        res = list_owners()
        exit(1)        

    if 'owner' == COMMAND:

        # list
        res = get_owner()
        exit(1)         

# Entry point
if __name__ == "__main__": 
    parse_input( sys.argv )
