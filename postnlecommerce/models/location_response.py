# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper
from postnlecommerce.models.get_locations_result_1 import GetLocationsResult1


class LocationResponse(object):

    """Implementation of the 'locationResponse' model.

    TODO: type model description here.

    Attributes:
        get_locations_result (GetLocationsResult1): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "get_locations_result": 'GetLocationsResult'
    }

    _optionals = [
        'get_locations_result',
    ]

    def __init__(self,
                 get_locations_result=APIHelper.SKIP):
        """Constructor for the LocationResponse class"""

        # Initialize members of the class
        if get_locations_result is not APIHelper.SKIP:
            self.get_locations_result = get_locations_result 

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
        get_locations_result = GetLocationsResult1.from_dictionary(dictionary.get('GetLocationsResult')) if 'GetLocationsResult' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(get_locations_result)
