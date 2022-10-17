import render_owners
import render_services

# TODO: Row testing code required to cleanup
# take input payload from user as a json

# resp = render_owners.list_authorized_users_and_teams()
# print(resp.text)

# d_obj["owner_id"] = ""
# resp = render_owners.retrieve_user_or_team(d_obj)
# print(resp.text)


# resp = render_services.list_services()
# print(resp)
# print(resp.text)
# print(resp.json())


# d_obj[""] = ""
# resp = render_services.create_service(d_obj)
# print(resp)


# d_obj[""] = ""
# resp = render_services.retrieve_service(d_obj)
# print(resp)


# d_obj[""] = ""
# resp = render_services.update_service(d_obj)
# print(resp)


# d_obj[""] = ""
# resp = update_service(d_obj)
# print(resp)



import requests

url = "https://api.render.com/v1/services"

payload = {
    "autoDeploy": "yes",
    "serviceDetails": {
        "pullRequestPreviewsEnabled": "no",
        "disk": {
            "sizeGB": 1,
            "name": "disk"
        },
        "envSpecificDetails": {
            "buildCommand": "pip install -r requirements.txt",
            "startCommand": "flask run"
        },
        "numInstances": 1,
        "plan": "starter",
        "region": "oregon",
        "env": "python"
    },
    "type": "web_service",
    "name": "flask-demo-api",
    "ownerId": "tea-ccts5053t398cocksqd0",
    "repo": "https://github.com/app-generator/sample-flask-stripe",
    "branch": "master"
}
headers = {
    "accept": "application/json",
    "content-type": "application/json",
    "authorization": "Bearer 123123123132"
}

response = requests.post(url, json=payload, headers=headers)

print(response.text)