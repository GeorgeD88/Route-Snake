# * On Google maps, you can set to arrive by a certain time and see how long the trip will take
# * or what time you should leave to get there on time. The problem is once you add more destinations
# * to your trip, suddenly that feature disappears. This program aims to target that specific feature
# * and fill the gap using a combination of the Distance Matrix API and the Directions API.
from credentials import *
import googlemaps  # try this later
import requests
import json


# Distance Matrix API
dismatrix_endpoint = "https://maps.googleapis.com/maps/api/distancematrix/json?"
dismatrix_parameters = {}

# Directions API
directions_endpoint = "https://maps.googleapis.com/maps/api/distancematrix/json?"
directions_parameters = {}
