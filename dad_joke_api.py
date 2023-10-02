import requests


def connection():
    url = 'https://icanhazdadjoke.com'
    headers = {
        'Accept': 'application/json'
    }
    response = requests.get(url=url, headers=headers)
    return response.json()['joke']

