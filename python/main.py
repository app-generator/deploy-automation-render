import render_owners
import render_services

resp = render_owners.list_authorized_users_and_teams()
print(resp.text)

# d_obj["owner_id"] = ""
# resp = render_owners.retrieve_user_or_team(d_obj)
# print(resp.text)


# resp = list_services()
# print(resp)
# print(resp.text)
# print(resp.json())


# d_obj[""] = ""
# resp = create_service(d_obj)
# print(resp)


# d_obj[""] = ""
# resp = retrieve_service(d_obj)
# print(resp)


# d_obj[""] = ""
# resp = update_service(d_obj)
# print(resp)


# d_obj[""] = ""
# resp = update_service(d_obj)
# print(resp)