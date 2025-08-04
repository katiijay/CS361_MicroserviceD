import requests
from .config import Config


def get_request(url=str, params=dict):
    # handles request to API. 
    responses = requests.get(url=url, params=params)
    return responses.json()

def get_activities(parkcode=str):
    # API variables
    url = 'https://developer.nps.gov/api/v1/thingstodo'
    params = {
        'api_key': Config.api_key,
        'parkcode': parkcode,
        'start': 0,
        'limit': 1
        }
    # creates a request string to determine how many results there are. 
    api_call = requests.get(url=url, params=params)
    api_results = api_call.json()
    total = int(api_results['total'])

    # while loop to handle api call result limit. 
    params['limit'] = 50
    api_results = []
    while params['start'] < total:
        api_call = requests.get(url=url, params=params)
        for value in api_call.json()['data']:
            api_results.append({
                'name': value['activities'][0]['name'],
                'shortDescription': value['shortDescription'],
                'longDescription': value['longDescription'],
                'url': value['url']
                })
        # update start to look for next 50 instances. 
        params['start'] += params['limit']

    return api_results



def get_all_activities():
    # API variables
    url = 'https://developer.nps.gov/api/v1/activities'
    params = {
        'api_key': Config.api_key,
        'start': 0,
        'limit': 1
        }
    # creates a request string to determine how many results there are. 
    api_call = requests.get(url=url, params=params)
    api_results = api_call.json()
    total = int(api_results['total'])

    # while loop to handle api call result limit. 
    params['limit'] = 50
    api_results = []
    while params['start'] < total:
        api_call = requests.get(url=url, params=params)
        for value in api_call.json()['data']:
            api_results.append(value)

        # update start to look for next 50 instances. 
        params['start'] += params['limit']

    return api_results