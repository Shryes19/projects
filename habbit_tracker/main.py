import requests,datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "shryes"
TOKEN = "hrfhbwrbvbjerv"

parameters = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}

#responce = requests.post(url=pixela_endpoint, json=parameters)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_parameters = {
    "id":"graph1",
    "name":"coding graph",
    "unit":"hours",
    "type":"float",
    "color":"ajisai",
}
headers = {
    "X-USER-TOKEN":TOKEN
}

# responce = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(responce.text)

pixela_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"
date = datetime.datetime(year=2024, month=8, day=11)

pixel_parameters = {
    "date":date.strftime("%Y%m%d"),
    "quantity":"2.50",
}

responce = requests.post(url=pixela_creation_endpoint,json=pixel_parameters, headers=headers)
print(responce.text)

pixela_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/{date.strftime('%Y%m%d')}"

update_parameters = {
        "quantity":"24"
}


responce = requests.put(url=pixela_update_endpoint,json=update_parameters, headers=headers)
print(responce.text)

