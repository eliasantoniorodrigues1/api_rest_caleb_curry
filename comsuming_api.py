import requests
import json

# You need do to have acces to the link of an API to comsume it...
url = "https://api.stackexchange.com/2.2/questions?order=desc&sort=activity&site=stackoverflow"

response = requests.get(url)
data = response.json()['items']

# you can create an application to search for good questions to answer.
for question in data:
    if question['answer_count'] == 0:
        print(question['title'])
        print(question['link'])
        print()
