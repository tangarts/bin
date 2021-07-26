#!/usr/bin/env python3
import requests
import json

# docs: https://www.reddit.com/dev/api#section_listings

base_url = "https://www.reddit.com/"

client_id = "ZEHgQDp1Idrtrw"
client_secret = "zbeP_2bHkanYQqQlb5Yjhu4-6J6Bwg"
password = "4F1e9MkTwK8sJQaQ3IBw"
user_agent = "proseporn by u/tangcam"
username = "tangcam"

data = {
    "grant_type": "password",
    "username": username,
    "password": password,
}

auth = requests.auth.HTTPBasicAuth(client_id, client_secret)
r = requests.post(
    base_url + "api/v1/access_token",
    data=data,
    headers={"user-agent": user_agent},
    auth=auth,
)

d = r.json()
token = 'bearer ' + d['access_token']
api_url = 'https://oauth.reddit.com'

headers = {'Authorization': token, 'User-Agent': user_agent}

payload = {'limit': 5, 'count': 0}
response = requests.get(
        api_url + '/r/ProsePorn/random',
        # params=payload,
        headers=headers,
        )
values = response.json()
data = values[0]['data']['children'][0]['data']
entry = {k: data[k] for k in ('id', 'title', 'selftext') if k in data}

with open('/home/nehe/doc/data/prosep.txt', 'a') as json_file:
    json.dump(entry, json_file)
    json_file.write("\n")

print(entry['title']+"\n")
print(entry['selftext'])
