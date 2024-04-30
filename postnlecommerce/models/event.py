# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper


class Event(object):

    """Implementation of the 'Event' model.

    TODO: type model description here.

    Attributes:
        code (str): The event code
        description (str): The event description
        destination_location_code (str): Location code of the destination
        location_code (str): The current location code
        route_code (str): The route code
        route_number (str): The route number
        time_stamp (str): Timestamp of the event

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "code": 'Code',
        "description": 'Description',
        "destination_location_code": 'DestinationLocationCode',
        "location_code": 'LocationCode',
        "route_code": 'RouteCode',
        "route_number": 'RouteNumber',
        "time_stamp": 'TimeStamp'
    }

    _optionals = [
        'code',
        'description',
        'destination_location_code',
        'location_code',
        'route_code',
        'route_number',
        'time_stamp',
    ]

    def __init__(self,
                 code=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 destination_location_code=APIHelper.SKIP,
                 location_code=APIHelper.SKIP,
                 route_code=APIHelper.SKIP,
                 route_number=APIHelper.SKIP,
                 time_stamp=APIHelper.SKIP):
        """Constructor for the Event class"""

        # Initialize members of the class
        if code is not APIHelper.SKIP:
            self.code = code 
        if description is not APIHelper.SKIP:
            self.description = description 
        if destination_location_code is not APIHelper.SKIP:
            self.destination_location_code = destination_location_code 
        if location_code is not APIHelper.SKIP:
            self.location_code = location_code 
        if route_code is not APIHelper.SKIP:
            self.route_code = route_code 
        if route_number is not APIHelper.SKIP:
            self.route_number = route_number 
        if time_stamp is not APIHelper.SKIP:
            self.time_stamp = time_stamp 

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
        code = dictionary.get("Code") if dictionary.get("Code") else APIHelper.SKIP
        description = dictionary.get("Description") if dictionary.get("Description") else APIHelper.SKIP
        destination_location_code = dictionary.get("DestinationLocationCode") if dictionary.get("DestinationLocationCode") else APIHelper.SKIP
        location_code = dictionary.get("LocationCode") if dictionary.get("LocationCode") else APIHelper.SKIP
        route_code = dictionary.get("RouteCode") if dictionary.get("RouteCode") else APIHelper.SKIP
        route_number = dictionary.get("RouteNumber") if dictionary.get("RouteNumber") else APIHelper.SKIP
        time_stamp = dictionary.get("TimeStamp") if dictionary.get("TimeStamp") else APIHelper.SKIP
        # Return an object of this model
        return cls(code,
                   description,
                   destination_location_code,
                   location_code,
                   route_code,
                   route_number,
                   time_stamp)
