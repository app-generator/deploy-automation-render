# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os

NODE_12="12.0.0"
NODE_14="14.0.0"
NODE_16="16.10.0"
NODE_18="18.0.0"

# Render authentication API
DEBUG = os.getenv("DEBUG")

# Render authentication API
RENDER_BUILDER = os.getenv("RENDER_BUILDER", 'npm')

if 'yarn' == RENDER_BUILDER.lower():
    RENDER_BUILDER = 'yarn' 
else:
    RENDER_BUILDER = 'npm'

# Render authentication API
RENDER_API_KEY = os.getenv("RENDER_API_KEY")

# Render authentication API
RENDER_OWNER_ID = os.getenv("RENDER_OWNER_ID")

# Entry points 
ENTRY_POINT_DJANGO = 'core.wsgi:application'
ENTRY_POINT_FLASK  = 'run:app' 
ENTRY_POINT_NODEJS = 'app.js'

# api header
HEADERS = {
    'accept': 'application/json',
    'authorization': f'Bearer {RENDER_API_KEY}',
}

# api url
URL="https://api.render.com"
