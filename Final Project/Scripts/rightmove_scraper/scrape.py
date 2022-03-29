import argparse
from datetime import datetime
import json
import logging
import math
from pathlib import Path
import pickle
from distutils.util import strtobool
import requests

# with open(Path(r"C:\Users\jwpow\PycharmProjects\rightmove_scraper\assets") / 'outcodeData.json', "r") as f:
with open(Path(__file__).resolve().parent / 'assets/outcodeData.json', "r") as f:
    outcode_data = json.load(f)
    outcode_data = {d.get('outcode'): d.get('code') for d in outcode_data}

HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}



def get_location_search_url(input_term):
    """
    Used to translate a location search term (eg Twickenham) into a relevant input for the Rightmove API.
    """
    location_identifier = ''
    count = 0

    for char in input_term:
        if count == 2:
            location_identifier += '/'
            count = 0
        location_identifier += char.upper()
        count += 1

    return location_identifier

x = get_location_search_url('London')


def get_location_id(input_term, input_outcode_mappings, postcode):
    """
    Returns a Rightmove location ID given either a search term (eg Twickenham) or postcode (eg TW1).
    """

    if postcode:
        return input_outcode_mappings[input_term]

    code_url = "https://www.rightmove.co.uk/typeAhead/uknostreet/"
    location_search_url = get_location_search_url(input_term)
    possible_locations = requests.get(code_url + location_search_url).json()

    return possible_locations['typeAheadLocations'][0]['locationIdentifier']

x = get_location_id('London','','')

y = requests.get('https://www.rightmove.co.uk/typeAhead/uknostreet + x').json()
print(y)


def make_request(user_input, postcode, sale_rent, params=None, index=0, radius=1.0):
    """
    Constructs an API request to the Rightmove API and returns the JSON response.

    sale_rent needs to be either "sale" or "rent".
    """
    api_root = f"https://api.rightmove.co.uk/api/{sale_rent}/find?"

    location_id = get_location_id(
        user_input,
        outcode_data,
        postcode=postcode
    )

    if postcode:
        location_id = f"OUTCODE%5E{location_id}"

    url_params = {
        "index": index * 25,
        "apiApplication": "IPAD",
        "locationIdentifier": location_id
    }

    if not postcode:
        url_params["radius"] = str(radius)

    if params is not None:
        url_params = {**url_params, **params}

    response = requests.get(api_root, params=url_params, headers=HEADERS)

    return response.json()


def save_property_data(properties: list, filename: str):
    """
    Dumps the returned list of dicts to the output directory, as a JSON object

    :param properties: list, returned property data
    :param filename:    string, name of file to be saved
    """
    with open(Path(__file__).resolve().parent / f'output/{filename}.json', "w") as f_out:
        json.dump(properties, f_out, indent=4)


def get_properties(input_location: str, postcode: bool, sale_rent: str="sale", radius: float=1.0):
    """
    Main function that incorporates all the other functions to make the request and loop over the responses to collect
    all available property data for that search term.

    :param input_location:  str, either a place ("Twickenham") or first part of a postcode ("TW1")
    :param postcode:        bool, True or False, depending what is supplied in input_location
    :param sale_rent:       str, either "sale" or "rent" depending on if you want to retrieve properties for sale or
                            for rent.
    :param radius:          float, search radius in miles. This only works if it is NOT a postcode.
    :return:                list, of dicts containing property data.
    """

    response_data = make_request(input_location, postcode=postcode, sale_rent=sale_rent)
    total_results = response_data['totalAvailableResults']
    required_pages = int(math.ceil(total_results / 24))
    properties = response_data['properties']

    for page_no in range(1, required_pages + 1):
        try:
            properties += make_request(input_location, postcode=postcode, sale_rent=sale_rent, index=page_no, radius=radius)['properties']
        except:
            continue

    return properties


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Process scraper inputs.')
    parser.add_argument('-l', '--input_location', type=str)
    parser.add_argument('-p', '--postcode', type=strtobool)
    parser.add_argument('-r', '--radius', type=float, default=1.0)
    parser.add_argument('-s', '--sale_rent', type=str, default="sale")

    args = parser.parse_args()

    input_location = args.input_location
    postcode = bool(args.postcode)
    radius = args.radius
    sale_rent = args.sale_rent


    if postcode:
        input_location = input_location.upper()

    properties = get_properties(
        input_location=input_location,
        postcode=postcode,
        sale_rent=sale_rent,
        radius=radius
    )

    timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    file_name = f'{timestamp} - {input_location} - {sale_rent}'

    if len(properties) > 0:
        save_property_data(properties, file_name)
