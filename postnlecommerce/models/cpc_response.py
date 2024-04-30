# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper


class CpcResponse(object):

    """Implementation of the 'cpcResponse' model.

    TODO: type model description here.

    Attributes:
        city (str): City of requested address
        postal_code (str): Postalcode of requested address
        street_name (str): Street of requested address
        house_number (int): Housenumber of requested address
        formatted_address (List[str]): Full formatted address according to
            PostNL standard (returns each line as a separate string)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "city": 'city',
        "postal_code": 'postalCode',
        "street_name": 'streetName',
        "house_number": 'houseNumber',
        "formatted_address": 'formattedAddress'
    }

    _optionals = [
        'city',
        'postal_code',
        'street_name',
        'house_number',
        'formatted_address',
    ]

    def __init__(self,
                 city=APIHelper.SKIP,
                 postal_code=APIHelper.SKIP,
                 street_name=APIHelper.SKIP,
                 house_number=APIHelper.SKIP,
                 formatted_address=APIHelper.SKIP):
        """Constructor for the CpcResponse class"""

        # Initialize members of the class
        if city is not APIHelper.SKIP:
            self.city = city 
        if postal_code is not APIHelper.SKIP:
            self.postal_code = postal_code 
        if street_name is not APIHelper.SKIP:
            self.street_name = street_name 
        if house_number is not APIHelper.SKIP:
            self.house_number = house_number 
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

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        city = dictionary.get("city") if dictionary.get("city") else APIHelper.SKIP
        postal_code = dictionary.get("postalCode") if dictionary.get("postalCode") else APIHelper.SKIP
        street_name = dictionary.get("streetName") if dictionary.get("streetName") else APIHelper.SKIP
        house_number = dictionary.get("houseNumber") if dictionary.get("houseNumber") else APIHelper.SKIP
        formatted_address = dictionary.get("formattedAddress") if dictionary.get("formattedAddress") else APIHelper.SKIP
        # Return an object of this model
        return cls(city,
                   postal_code,
                   street_name,
                   house_number,
                   formatted_address)
