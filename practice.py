import requests

api_key = '28aeb0df-a3fa-4da1-b800-5060166fc6ab'
word = 'tomato'
url = f'https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}'

res = requests.get(url)

definitions = res.json()

for definition in definitions:
    print(definition)
