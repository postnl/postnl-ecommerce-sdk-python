# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper
from postnlecommerce.models.get_locations_result_multiple import GetLocationsResultMultiple


class LocationsResponseMultiple(object):

    """Implementation of the 'locationsResponseMultiple' model.

    Attributes:
        get_locations_result (GetLocationsResultMultiple): The model property
            of type GetLocationsResultMultiple.

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
        """Constructor for the LocationsResponseMultiple class"""

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

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        get_locations_result = GetLocationsResultMultiple.from_dictionary(dictionary.get('GetLocationsResult')) if 'GetLocationsResult' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(get_locations_result)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'get_locations_result={(self.get_locations_result if hasattr(self, "get_locations_result") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'get_locations_result={(self.get_locations_result if hasattr(self, "get_locations_result") else None)!s})')
