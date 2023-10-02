import requests


def connection():
    try:
        url = 'https://icanhazdadjoke.com'
        headers = {
            'Accept': 'application/json'
        }
        response = requests.get(url=url, headers=headers)
        return response.json()['joke']
    except requests.ConnectionError:
        return "error connection"
    except requests.Timeout:
        return "Time Out while trying to connect to API"
    except requests.RequestException as e:
        return f"Error : {e}"
    except Exception as exception:
        return f"Error :{exception}"
