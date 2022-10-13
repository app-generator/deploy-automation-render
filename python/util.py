import os

# Render authentication API
RENDER_API_KEY = os.environ.get("RENDER_API_KEY", "")

# api header
HEADERS = {
    'Accept': 'application/json',
    'Authorization': f'Bearer {RENDER_API_KEY}',
}

# api url
URL="https://api.render.com"