from requests import get, post, put, delete

url = "http://127.0.0.1:5000/api/"

print(post(url, json={"nome":"Raspberry PI"}))

print(delete(url, json={"nome":'arduino uno', 'id': "9c2309dc-13f7-49a9-96c4-cca1186d7cbf"}).json())