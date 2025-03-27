# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper


class MethodNotAllowedOnlyGetPostCheckoutPostalcodeCheckAPI(object):

    """Implementation of the 'MethodNotAllowedOnlyGetPost_Checkout Postalcode Check API' model.

    Attributes:
        message (str): The model property of type str.
        http_status_code (float): The model property of type float.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "message": 'message',
        "http_status_code": 'http_status_code'
    }

    _optionals = [
        'message',
        'http_status_code',
    ]

    def __init__(self,
                 message=APIHelper.SKIP,
                 http_status_code=APIHelper.SKIP):
        """Constructor for the MethodNotAllowedOnlyGetPostCheckoutPostalcodeCheckAPI class"""

        # Initialize members of the class
        if message is not APIHelper.SKIP:
            self.message = message 
        if http_status_code is not APIHelper.SKIP:
            self.http_status_code = http_status_code 

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
        message = dictionary.get("message") if dictionary.get("message") else APIHelper.SKIP
        http_status_code = dictionary.get("http_status_code") if dictionary.get("http_status_code") else APIHelper.SKIP
        # Return an object of this model
        return cls(message,
                   http_status_code)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'message={(self.message if hasattr(self, "message") else None)!r}, '
                f'http_status_code={(self.http_status_code if hasattr(self, "http_status_code") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'message={(self.message if hasattr(self, "message") else None)!s}, '
                f'http_status_code={(self.http_status_code if hasattr(self, "http_status_code") else None)!s})')
