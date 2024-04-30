# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper
from postnlecommerce.models.address_1 import Address1
from postnlecommerce.models.opening_hours import OpeningHours
from postnlecommerce.models.sustainability import Sustainability


class Location(object):

    """Implementation of the 'Location' model.

    TODO: type model description here.

    Attributes:
        address (Address1): The pickup location address
        pickup_time (str): Time from when the parcel can be retrieved at the
            pickup location
        opening_hours (OpeningHours): The standard opening hours of the pickup
            location
        distance (int): The calculated distance (in meters) between the
            location specified and the address provided in the request
        location_code (str): The location identifier
        partner_id (str): The partner identifier; not used anymore
        sustainability (Sustainability): Sustainability score; see
            [Sustainability codes](#tag/Reference-codes/Sustainability-codes)
            for possible values.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "address": 'Address',
        "pickup_time": 'PickupTime',
        "opening_hours": 'OpeningHours',
        "distance": 'Distance',
        "location_code": 'LocationCode',
        "partner_id": 'PartnerID',
        "sustainability": 'Sustainability'
    }

    _optionals = [
        'address',
        'pickup_time',
        'opening_hours',
        'distance',
        'location_code',
        'partner_id',
        'sustainability',
    ]

    def __init__(self,
                 address=APIHelper.SKIP,
                 pickup_time=APIHelper.SKIP,
                 opening_hours=APIHelper.SKIP,
                 distance=APIHelper.SKIP,
                 location_code=APIHelper.SKIP,
                 partner_id=APIHelper.SKIP,
                 sustainability=APIHelper.SKIP):
        """Constructor for the Location class"""

        # Initialize members of the class
        if address is not APIHelper.SKIP:
            self.address = address 
        if pickup_time is not APIHelper.SKIP:
            self.pickup_time = pickup_time 
        if opening_hours is not APIHelper.SKIP:
            self.opening_hours = opening_hours 
        if distance is not APIHelper.SKIP:
            self.distance = distance 
        if location_code is not APIHelper.SKIP:
            self.location_code = location_code 
        if partner_id is not APIHelper.SKIP:
            self.partner_id = partner_id 
        if sustainability is not APIHelper.SKIP:
            self.sustainability = sustainability 

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
        address = Address1.from_dictionary(dictionary.get('Address')) if 'Address' in dictionary.keys() else APIHelper.SKIP
        pickup_time = dictionary.get("PickupTime") if dictionary.get("PickupTime") else APIHelper.SKIP
        opening_hours = OpeningHours.from_dictionary(dictionary.get('OpeningHours')) if 'OpeningHours' in dictionary.keys() else APIHelper.SKIP
        distance = dictionary.get("Distance") if dictionary.get("Distance") else APIHelper.SKIP
        location_code = dictionary.get("LocationCode") if dictionary.get("LocationCode") else APIHelper.SKIP
        partner_id = dictionary.get("PartnerID") if dictionary.get("PartnerID") else APIHelper.SKIP
        sustainability = Sustainability.from_dictionary(dictionary.get('Sustainability')) if 'Sustainability' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(address,
                   pickup_time,
                   opening_hours,
                   distance,
                   location_code,
                   partner_id,
                   sustainability)
