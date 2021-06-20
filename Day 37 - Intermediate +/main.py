import requests
from datetime import datetime

USERNAME = USERNAME
TOKEN = TOKEN

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",  # should be "no", but I used "yes" because I cant use the service otherwise.
}
# STEP 1 ---------- Creating a user. https://docs.pixe.la/entry/post-user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# STEP 2 ---------- Creating a graph. https://docs.pixe.la/entry/post-graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "hours",
    "type": "float",
    "color": "shibafu",
}

headers = {
    "X-USER-TOKEN": TOKEN
}
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# STEP 3 ---------- Create a new pixel. https://docs.pixe.la/entry/post-pixel

today = datetime.now()
# print(today.strftime("%Y%m%d")) # - https://www.w3schools.com/python/python_datetime.asp

pixel_creation_endpoint = f"{graph_endpoint}/graph1"

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours have you coded today?: "),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_params, headers=headers)
print(response.text)

# STEP 4 ---------- Changing an existing pixel. https://docs.pixe.la/entry/put-pixel

editing_pixel_endpoint = f"{pixel_creation_endpoint}/{today.strftime('%Y%m%d')}"

new_pixel_params = {
    "quantity": "3",
}

# response = requests.put(url=editing_pixel_endpoint, json=new_pixel_params, headers=headers)
# print(response.text)

# STEP 5 ---------- Deleting A Pixel. https://docs.pixe.la/entry/delete-pixel

# delete_pixel_endpoint = editing_pixel_endpoint
#
# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)
