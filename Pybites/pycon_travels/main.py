import json
from dataclasses import dataclass
from datetime import datetime
from math import acos, cos, radians, sin
import os
from pathlib import Path
from urllib.request import urlretrieve
from pprint import pprint
import re

from dateutil.parser import parse

URL = "https://bites-data.s3.us-east-2.amazonaws.com/pycons-europe-2019.json"
RESPONSES = "https://bites-data.s3.us-east-2.amazonaws.com/nominatim_responses.json"

tmp = Path(os.getenv("TMP", "/tmp"))
pycons_file = tmp / "pycons-europe-2019.json"
nominatim_responses = tmp / "nominatim_responses.json"

if not pycons_file.exists() or not nominatim_responses.exists():
    urlretrieve(URL, pycons_file)
    urlretrieve(RESPONSES, nominatim_responses)


@dataclass
class PyCon:
    name: str
    city: str
    country: str
    start_date: datetime
    end_date: datetime
    URL: str
    lat: float = None
    lon: float = None


@dataclass
class Trip:
    origin: PyCon
    destination: PyCon
    distance: float


def _get_pycons():
    """Helper function that retrieves required PyCon data
       and returns a list of PyCon objects
    """
    with open(pycons_file, "r", encoding="utf-8") as f:
        return [
            PyCon(
                pycon["name"],
                pycon["city"],
                pycon["country"],
                parse(pycon["start_date"]),
                parse(pycon["end_date"]),
                pycon["url"],
            )
            for pycon in json.load(f)
        ]


def _km_distance(origin, destination):
    """ Helper function that retrieves the air distance in kilometers for two pycons """
    lon1, lat1, lon2, lat2 = map(
        radians, [origin.lon, origin.lat, destination.lon, destination.lat]
    )
    return 6371 * (
        acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lon1 - lon2))
    )


# Your code #
def update_pycons_lat_lon(pycons):
    """
    Update the latitudes and longitudes based on the city and country
    the PyCon takes places. Use requests from the Nominatim API stored in the
    nominatim_responses json file.
    """
    pattern = 'q=(.*)&format'
    city_country_dict = create_city_country_dict(nominatim_resp_json, pattern)
    
    for pycon in pycons:
        pycon_city, pycon_country = pycon.city, pycon.country
        city_country_str = pycon.city + ',' + pycon.country
        
        city_country_url = city_country_dict[city_country_str]
        
        nominatim_resp_values = nominatim_resp_json[city_country_url][0]
        
        for nominatim_resp_key, nominatim_resp_value in nominatim_resp_values.items():
            if nominatim_resp_key == 'lat':
                pycon_lat = float(nominatim_resp_value)
                pycon.lat = pycon_lat
            elif nominatim_resp_key == 'lon':
                pycon_lon = float(nominatim_resp_value)
                pycon.lon = pycon_lat
    
    return pycons


def create_travel_plan(pycons):
    """
    Create your travel plan to visit all the PyCons.
    Assume it's now the start of 2019!
    Return a list of Trips with each Trip containing the origin PyCon,
    the destination PyCon and the travel distance between the PyCons.
    """
    update_pycons_lat_lon(pycons)
    sorted(pycons, key = lambda x: (x.start_date, x.end_date))
    trip_data = [Trip(origin = pycons[i], destination = pycons[i+1], distance = _km_distance(pycons[i], pycons[i+1])) for i in range(0,len(pycons)-1)]
    return trip_data


def total_travel_distance(journey):
    """
    Return the total travel distance of your PyCon journey in kilometers
    rounded to one decimal.
    """
    distance = [x.distance for x in journey]
    
    return distance

def create_city_country_dict(resp_json, pattern):
    city_country_url = dict()
    
    for url, values in nominatim_resp_json.items():
        city_country = re.findall(pattern, url)[0]
        city_country_url[city_country] = url
    
    return city_country_url



with open(nominatim_responses, 'r') as f:
    nominatim_resp_json = json.load(f)

pycons = _get_pycons()
update_pycons_lat_lon(pycons)
travel_plan = create_travel_plan(pycons)
pprint(total_travel_distance(travel_plan))