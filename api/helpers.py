# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import requests
import random, string

from .common   import *

def randStr( aLen=5 ):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=aLen )).lower()

def nameFromRepo( aRepoURL ):

    if not aRepoURL:
        return aRepoURL

    aRepoURL = aRepoURL.replace('.git', '')
    return aRepoURL.split('/')[-1]
