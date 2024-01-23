import requests
from datetime import datetime

USERNAME = "kanedgy"
TOKEN = "testtest"

pixela_end = 'https://pixe.la/v1/users'
user_param = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url= pixela_end, json=user_param)
# print(response.text)

graph_endpoint = f"{pixela_end}/{USERNAME}/graphs"
graph_config = {
    "id": "graph1",
    "name": "Study",
    "unit": "min",
    "type": "int",
    "color": "shibafu",
}
today = datetime.now()
today = today.strftime("%Y%m%d")
graph_post = f"{pixela_end}/{USERNAME}/graphs/graph1"
graph_post_config = {
    "id": "graph1",
    "date": today,
    "quantity": "150",
}
user_put = f"{pixela_end}/{USERNAME}/graphs/graph1/{today}"
user_put_config = {
    "quantity": "25",
    "pinnedGraphID": "graph1",
}

headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
update = requests.put(url=user_put, json=user_put_config, headers=headers)
print(update.text)