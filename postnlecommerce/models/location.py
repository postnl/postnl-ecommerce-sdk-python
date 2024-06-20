# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper
from postnlecommerce.models.delivery_options import DeliveryOptions
from postnlecommerce.models.locations_address import LocationsAddress
from postnlecommerce.models.locations_opening_hours import LocationsOpeningHours
from postnlecommerce.models.sustainability import Sustainability


class Location(object):

    """Implementation of the 'location' model.

    TODO: type model description here.

    Attributes:
        address (LocationsAddress): TODO: type description here.
        delivery_options (DeliveryOptions): The options belonging to the
            pickup location. The delivery options RETA, UL, PU, DO, BW, RT and
            BWUL can be shown in the response. Please ignore these codes.
            These codes are internal PostNL codes.
        distance (int): The distance from the address/coordinates provided in
            the request to the pickup location returned. Distance in meters.
        latitude (float): The latitude of the pickup location
        location_code (int): The pickup location identifier
        longitude (float): The longitude of the pickup location
        name (str): The name of the pickup location
        opening_hours (LocationsOpeningHours): The standard opening times of
            the pickup location
        sustainability (Sustainability): Sustainability score; see
            [Sustainability
            codes](https://developer.postnl.nl/docs/#/http/reference-data/refer
            ence-codes/sustainability-codes) for possible values.
        partner_name (str): The partner name belonging to the pickup location.
            Can be ignored, no longer used.
        retail_network_id (str): The retail network belonging to the pickup
            location. Can be ignored, no longer used

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "address": 'Address',
        "delivery_options": 'DeliveryOptions',
        "distance": 'Distance',
        "latitude": 'Latitude',
        "location_code": 'LocationCode',
        "longitude": 'Longitude',
        "name": 'Name',
        "opening_hours": 'OpeningHours',
        "sustainability": 'Sustainability',
        "partner_name": 'PartnerName',
        "retail_network_id": 'RetailNetworkID'
    }

    _optionals = [
        'address',
        'delivery_options',
        'distance',
        'latitude',
        'location_code',
        'longitude',
        'name',
        'opening_hours',
        'sustainability',
        'partner_name',
        'retail_network_id',
    ]

    def __init__(self,
                 address=APIHelper.SKIP,
                 delivery_options=APIHelper.SKIP,
                 distance=APIHelper.SKIP,
                 latitude=APIHelper.SKIP,
                 location_code=APIHelper.SKIP,
                 longitude=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 opening_hours=APIHelper.SKIP,
                 sustainability=APIHelper.SKIP,
                 partner_name=APIHelper.SKIP,
                 retail_network_id=APIHelper.SKIP):
        """Constructor for the Location class"""

        # Initialize members of the class
        if address is not APIHelper.SKIP:
            self.address = address 
        if delivery_options is not APIHelper.SKIP:
            self.delivery_options = delivery_options 
        if distance is not APIHelper.SKIP:
            self.distance = distance 
        if latitude is not APIHelper.SKIP:
            self.latitude = latitude 
        if location_code is not APIHelper.SKIP:
            self.location_code = location_code 
        if longitude is not APIHelper.SKIP:
            self.longitude = longitude 
        if name is not APIHelper.SKIP:
            self.name = name 
        if opening_hours is not APIHelper.SKIP:
            self.opening_hours = opening_hours 
        if sustainability is not APIHelper.SKIP:
            self.sustainability = sustainability 
        if partner_name is not APIHelper.SKIP:
            self.partner_name = partner_name 
        if retail_network_id is not APIHelper.SKIP:
            self.retail_network_id = retail_network_id 

    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object
            as obtained from the deserialization of the server's response. The
            keys MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        address = LocationsAddress.from_dictionary(dictionary.get('Address')) if 'Address' in dictionary.keys() else APIHelper.SKIP
        delivery_options = DeliveryOptions.from_dictionary(dictionary.get('DeliveryOptions')) if 'DeliveryOptions' in dictionary.keys() else APIHelper.SKIP
        distance = dictionary.get("Distance") if dictionary.get("Distance") else APIHelper.SKIP
        latitude = dictionary.get("Latitude") if dictionary.get("Latitude") else APIHelper.SKIP
        location_code = dictionary.get("LocationCode") if dictionary.get("LocationCode") else APIHelper.SKIP
        longitude = dictionary.get("Longitude") if dictionary.get("Longitude") else APIHelper.SKIP
        name = dictionary.get("Name") if dictionary.get("Name") else APIHelper.SKIP
        opening_hours = LocationsOpeningHours.from_dictionary(dictionary.get('OpeningHours')) if 'OpeningHours' in dictionary.keys() else APIHelper.SKIP
        sustainability = Sustainability.from_dictionary(dictionary.get('Sustainability')) if 'Sustainability' in dictionary.keys() else APIHelper.SKIP
        partner_name = dictionary.get("PartnerName") if dictionary.get("PartnerName") else APIHelper.SKIP
        retail_network_id = dictionary.get("RetailNetworkID") if dictionary.get("RetailNetworkID") else APIHelper.SKIP
        # Return an object of this model
        return cls(address,
                   delivery_options,
                   distance,
                   latitude,
                   location_code,
                   longitude,
                   name,
                   opening_hours,
                   sustainability,
                   partner_name,
                   retail_network_id)
