import requests, logger

def get_request(url):
    try:
        response = requests.get(url=url)
    except Exception as error:
        logger.log(error)
    return response

def get_request_json(url):
    try:
        response = requests.get(url=url)
        data = response.json()
    except Exception as error:
        logger.log(error)
    return data