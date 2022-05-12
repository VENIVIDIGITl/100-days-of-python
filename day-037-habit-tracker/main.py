import requests
from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_TOKEN = ""
PIXELA_USERNAME = ""
GRAPH_ID = ""

user_params = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
# print(response.text)

PIXEL_COLOR_OPTIONS = {
    "green": "shibafu",
    "red": "momiji",
    "blue": "sora",
    "yellow": "ichou",
    "purple": "ajisai",
    "black": "kuro"
}

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs"
GRAPH_TYPE = "int"  # or "float"
graph_config = {
    "id": GRAPH_ID,
    "name": "",
    "unit": "",
    "type": GRAPH_TYPE,
    "color": PIXEL_COLOR_OPTIONS["green"]
}

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

response = requests.patch(url=GRAPH_ENDPOINT, json=graph_config, headers=headers)
print(response.text)


UPDATE_GRAPH_CONFIG_ENDPOINT = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}"
update_graph_config = {
    "color": "blue"
}

# response = requests.put(url=UPDATE_GRAPH_CONFIG_ENDPOINT, json=update_graph_config, headers=headers)
# print(response.text)


PIXEL_CREATION_ENDPOINT = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}"
today = datetime.now()
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("Quantity: ? ")
}

# response = requests.post(url=PIXEL_CREATION_ENDPOINT, json=pixel_data, headers=headers)
# print(response.text)


update_yyyyMMdd = datetime(year=0000, month=0, day=0)
PIXEL_UPDATE_ENDPOINT = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}/{update_yyyyMMdd}"
update_pixel_data = {
    "quantity": ""
}

# response = requests.put(url=PIXEL_UPDATE_ENDPOINT, json=update_pixel_data, headers=headers)
# print(response.text)

delete_yyyyMMdd = datetime(year=0000, month=0, day=0)
PIXEL_DELETE_ENDPOINT = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs/{GRAPH_ID}/{delete_yyyyMMdd}"

# response = requests.delete(url=PIXEL_DELETE_ENDPOINT, headers=headers)
# print(response.text)
