import json
import requests
import re
from geopy.geocoders import Nominatim


def isvalid(postcode):
    """Validates Outcode and Incode"""
    if postcode.find(' ')==-1:
        return False
    code = postcode.split(" ")
    outward = code[0]
    inward = code[1]
    if postcode.find(' ')==False:
        return False
    if re.match("^[0-9][ABD-HJLNP-UW-Z]{2}$", inward) is None:
        return False
    if re.match("^[A-PR-UWYZ]{1}(([0-9]{1,2}|[0-9][A-HJKS-UW])|([A-HK-Y]{1}([0-9]{1,2}|[0-9][A-Z])))$", outward) is None:
        return False
    return True

def get_data(postcode):
    """
        Retrieve data from postcode api.
        API - https://api.postcodes.io/postcodes/
    """
    try:
        url = requests.get('https://api.postcodes.io/postcodes/' + postcode)
        data = json.loads(url.text)
        if data['status']==200:
            return data
        else:
            raise Exception(data['error']) 
    except requests.exceptions.RequestException as e:
        raise Exception(e)
        
def get_outward(postcode):
    
    ''''''
    if isvalid(postcode):
        out=postcode.split(' ')
        return out[0]
    else :
        raise Exception('Invalid Postcode')
     

def get_inward(postcode):
    if isvalid(postcode):
        res=postcode[-1:-4:-1]
        return res[2::-1]
    else :
        raise Exception('Invalid Postcode')

def get_address(postcode):
    geolocator = Nominatim(user_agent="ukadd")
    try:
        get_data(postcode)
        result = get_data(postcode)['result']
        location = geolocator.reverse(str(result["latitude"]) +"," + str(result["longitude"]))
        return location.address
    except Exception:
        raise Exception('No data found for given postcode')

