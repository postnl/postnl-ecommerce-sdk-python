# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper


class BarcodeError(object):

    """Implementation of the 'barcodeError' model.

    Attributes:
        error_msg (str): The error message
        error_number (str): The error code

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "error_msg": 'ErrorMsg',
        "error_number": 'ErrorNumber'
    }

    _optionals = [
        'error_msg',
        'error_number',
    ]

    def __init__(self,
                 error_msg=APIHelper.SKIP,
                 error_number=APIHelper.SKIP):
        """Constructor for the BarcodeError class"""

        # Initialize members of the class
        if error_msg is not APIHelper.SKIP:
            self.error_msg = error_msg 
        if error_number is not APIHelper.SKIP:
            self.error_number = error_number 

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
        error_msg = dictionary.get("ErrorMsg") if dictionary.get("ErrorMsg") else APIHelper.SKIP
        error_number = dictionary.get("ErrorNumber") if dictionary.get("ErrorNumber") else APIHelper.SKIP
        # Return an object of this model
        return cls(error_msg,
                   error_number)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'error_msg={(self.error_msg if hasattr(self, "error_msg") else None)!r}, '
                f'error_number={(self.error_number if hasattr(self, "error_number") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'error_msg={(self.error_msg if hasattr(self, "error_msg") else None)!s}, '
                f'error_number={(self.error_number if hasattr(self, "error_number") else None)!s})')
