# constants ==============
from credentials import *
from plus_codes import *
# ========================
# from openlocationcode import openlocationcode
import requests
import json


# Place Search API: Find Place request
place_search_endpoint = "https://maps.googleapis.com/maps/api/place/findplacefromtext/" \
"json?inputtype=textquery&%skey=" + PLACES_API_KEY


def search_places(place_name: str, raw_parameters: list = {"fields": ['name', 'plus_code'],
                 "locationbias": 'circle:%u@%f,%f' % (2000, UCF_COORDS[0], UCF_COORDS[1])}) -> dict:
    """
    This function searches a place based on text input and parameters

    # TODO: CONTINUE FILLING OUT THE DOCSTRING LATER
    Args:
        place_name (str): [description]
        parameters (list, optional): [description]. Defaults to {"fields": ['name', 'formatted_address'], "basic": ['plus_code'], "locationbias": 'circle:%u@%f,%f' % (RADIUS=2000, LATITUDE, LONGITUDE)}.

    Raises:
        Exception: [description]

    Returns:
        dict: [description]

    """

    raw_parameters['input'] = place_name
    # if 'plus_code' not in raw_parameters['fields']:
    #     raw_parameters['fields'].append('plus_code')

    # constructs the parameters portion of the HTTP request
    parameters = ''
    for param, value in raw_parameters.items():
        parameters += param.replace(' ', '+') + '='
        if type(value) == list:
            for sub_param in value:
                parameters += sub_param.replace(' ', '+') + ','
            parameters = parameters[:-1] + '&'
        else:
            parameters += value + '&'

    # HTTP request
    constr_url = place_search_endpoint % parameters
    data = requests.get(constr_url)
    # if OK response isn't received, raises "bad request error"
    if str(data) != '<Response [200]>':
        with open('error.json', 'w+') as out_file:
            json.dump(data.json(), out_file, indent=2)
        raise Exception('Bad Request: error ' + str(get_req))
    # otherwise if OK is received, it will return the result
    else:
        return data.json()
