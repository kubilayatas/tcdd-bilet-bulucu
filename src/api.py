import requests
import config

headers = {
    'Authorization': 'Basic ZGl0cmF2b3llYnNwOmRpdHJhMzQhdm8u'
}

def post_request(url, body):
    try:
        response = requests.post(url, json=body, headers=headers, timeout=5)
    except:
        print("Error occured, trying to continue...")
    return response
