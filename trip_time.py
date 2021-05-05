# constants ==============
from credentials import *
from plus_codes import *
# ========================
from find_location import *
import googlemaps  # try this later
import requests
import json


# * On Google maps, you can set to arrive by a certain time and see how long the trip will take
# * or what time you should leave to get there on time. The problem is once you add more destinations
# * to your trip, suddenly that feature disappears. This program aims to target that specific feature
# * and fill the gap using a combination of the Distance Matrix API and the Directions API.


# Distance Matrix API
dismatrix_endpoint = "https://maps.googleapis.com/maps/api/distancematrix/json?"
dismatrix_parameters = {}

# Directions API
directions_endpoint = "https://maps.googleapis.com/maps/api/distancematrix/json?"
directions_parameters = {}


def find_plus_code(place_name: str, raw_parameters: list = {"fields": ['name', 'plus_code'],  # TODO: review the parameters argument and determine the best default parameters needed for the task at hand
                 "locationbias": 'circle:%u@%f,%f' % (2000, UCF_COORDS[0], UCF_COORDS[1])}) -> str:
    """
    Extracts the plus code of a location from requested data from the Google Place Search API
        from a search based on the text input and parameters provided.

    # TODO: CONTINUE FILLING OUT THE DOCSTRING LATER
    Args:
        place_name (str): [description]

    Returns:
        str: [description]

    """
    if 'plus_code' not in raw_parameters['fields']:
        raw_parameters['fields'].append('plus_code')
    return search_places(place_name, raw_parameters)['candidates'][0]['plus_code']['global_code']
