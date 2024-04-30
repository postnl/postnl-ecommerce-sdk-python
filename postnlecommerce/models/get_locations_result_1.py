# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper
from postnlecommerce.models.location_1 import Location1


class GetLocationsResult1(object):

    """Implementation of the 'GetLocationsResult1' model.

    TODO: type model description here.

    Attributes:
        response_location (Location1): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "response_location": 'ResponseLocation'
    }

    _optionals = [
        'response_location',
    ]

    def __init__(self,
                 response_location=APIHelper.SKIP):
        """Constructor for the GetLocationsResult1 class"""

        # Initialize members of the class
        if response_location is not APIHelper.SKIP:
            self.response_location = response_location 

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
        response_location = Location1.from_dictionary(dictionary.get('ResponseLocation')) if 'ResponseLocation' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(response_location)
