# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper


class PostalcodeCheckAddress(object):

    """Implementation of the 'postalcodeCheckAddress' model.

    Attributes:
        city (str): City of requested address
        postal_code (str): Postalcode of requested address
        street_name (str): Street of requested address
        house_number (int): Housenumber of requested address
        house_number_addition (str): Housenumber addition
        formatted_address (List[str]): Full formatted address according to
            PostNL standard (returns each line as a separate string)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "city": 'city',
        "postal_code": 'postalCode',
        "street_name": 'streetName',
        "house_number": 'houseNumber',
        "house_number_addition": 'houseNumberAddition',
        "formatted_address": 'formattedAddress'
    }

    _optionals = [
        'city',
        'postal_code',
        'street_name',
        'house_number',
        'house_number_addition',
        'formatted_address',
    ]

    def __init__(self,
                 city=APIHelper.SKIP,
                 postal_code=APIHelper.SKIP,
                 street_name=APIHelper.SKIP,
                 house_number=APIHelper.SKIP,
                 house_number_addition=APIHelper.SKIP,
                 formatted_address=APIHelper.SKIP):
        """Constructor for the PostalcodeCheckAddress class"""

        # Initialize members of the class
        if city is not APIHelper.SKIP:
            self.city = city 
        if postal_code is not APIHelper.SKIP:
            self.postal_code = postal_code 
        if street_name is not APIHelper.SKIP:
            self.street_name = street_name 
        if house_number is not APIHelper.SKIP:
            self.house_number = house_number 
        if house_number_addition is not APIHelper.SKIP:
            self.house_number_addition = house_number_addition 
        if formatted_address is not APIHelper.SKIP:
            self.formatted_address = formatted_address 

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
        city = dictionary.get("city") if dictionary.get("city") else APIHelper.SKIP
        postal_code = dictionary.get("postalCode") if dictionary.get("postalCode") else APIHelper.SKIP
        street_name = dictionary.get("streetName") if dictionary.get("streetName") else APIHelper.SKIP
        house_number = dictionary.get("houseNumber") if dictionary.get("houseNumber") else APIHelper.SKIP
        house_number_addition = dictionary.get("houseNumberAddition") if dictionary.get("houseNumberAddition") else APIHelper.SKIP
        formatted_address = dictionary.get("formattedAddress") if dictionary.get("formattedAddress") else APIHelper.SKIP
        # Return an object of this model
        return cls(city,
                   postal_code,
                   street_name,
                   house_number,
                   house_number_addition,
                   formatted_address)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'city={(self.city if hasattr(self, "city") else None)!r}, '
                f'postal_code={(self.postal_code if hasattr(self, "postal_code") else None)!r}, '
                f'street_name={(self.street_name if hasattr(self, "street_name") else None)!r}, '
                f'house_number={(self.house_number if hasattr(self, "house_number") else None)!r}, '
                f'house_number_addition={(self.house_number_addition if hasattr(self, "house_number_addition") else None)!r}, '
                f'formatted_address={(self.formatted_address if hasattr(self, "formatted_address") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'city={(self.city if hasattr(self, "city") else None)!s}, '
                f'postal_code={(self.postal_code if hasattr(self, "postal_code") else None)!s}, '
                f'street_name={(self.street_name if hasattr(self, "street_name") else None)!s}, '
                f'house_number={(self.house_number if hasattr(self, "house_number") else None)!s}, '
                f'house_number_addition={(self.house_number_addition if hasattr(self, "house_number_addition") else None)!s}, '
                f'formatted_address={(self.formatted_address if hasattr(self, "formatted_address") else None)!s})')
