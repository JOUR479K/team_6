import requests.csv

access_token = 'ACCESS TOKEN'
client_secret = 'CLIENT SECRET'

api = InstagramAPI(access_token=access_token, client_secret=client_secret)


url = "https://api.instagram.com/v1/locations/search?lat=48.858844&lng=2.294351&access_token=ACCESS-TOKEN"

r = requests.get(url)
response = r.json()['data']

print response[0]['id']
print response[0]['latitude']
print response[0]['longitude']
print response[0]['name']
print response[0]['images']['thumbnail']['url']

for instagram in response:
	