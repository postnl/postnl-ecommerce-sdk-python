# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper


class Error(object):

    """Implementation of the 'Error' model.

    Attributes:
        error_code (str): The model property of type str.
        error_description (str): The model property of type str.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "error_code": 'ErrorCode',
        "error_description": 'ErrorDescription'
    }

    _optionals = [
        'error_code',
        'error_description',
    ]

    def __init__(self,
                 error_code=APIHelper.SKIP,
                 error_description=APIHelper.SKIP):
        """Constructor for the Error class"""

        # Initialize members of the class
        if error_code is not APIHelper.SKIP:
            self.error_code = error_code 
        if error_description is not APIHelper.SKIP:
            self.error_description = error_description 

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
        error_code = dictionary.get("ErrorCode") if dictionary.get("ErrorCode") else APIHelper.SKIP
        error_description = dictionary.get("ErrorDescription") if dictionary.get("ErrorDescription") else APIHelper.SKIP
        # Return an object of this model
        return cls(error_code,
                   error_description)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'error_code={(self.error_code if hasattr(self, "error_code") else None)!r}, '
                f'error_description={(self.error_description if hasattr(self, "error_description") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'error_code={(self.error_code if hasattr(self, "error_code") else None)!s}, '
                f'error_description={(self.error_description if hasattr(self, "error_description") else None)!s})')
