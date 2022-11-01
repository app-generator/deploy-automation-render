# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

import os

# Render authentication API
DEBUG = os.getenv("DEBUG")

# Render authentication API
RENDER_API_KEY = os.getenv("RENDER_API_KEY")

# api header
HEADERS = {
    'accept': 'application/json',
    'authorization': f'Bearer {RENDER_API_KEY}',
}

# api url
URL="https://api.render.com"

