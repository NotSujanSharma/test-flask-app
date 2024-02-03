import requests

def getData(url):
    try:
        response = requests.get(url)
        return response.text
    except requests.RequestException as e:
        return f"Error: {e}"

def postData(url, data):
    try:
        response = requests.post(url, data=data)
        return response.text
    except requests.RequestException as e:
        return f"Error: {e}"
