# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper


class ConfirmingError(object):

    """Implementation of the 'confirmingError' model.

    Attributes:
        code (str): The error code
        description (str): The error description

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "code": 'Code',
        "description": 'Description'
    }

    _optionals = [
        'code',
        'description',
    ]

    def __init__(self,
                 code=APIHelper.SKIP,
                 description=APIHelper.SKIP):
        """Constructor for the ConfirmingError class"""

        # Initialize members of the class
        if code is not APIHelper.SKIP:
            self.code = code 
        if description is not APIHelper.SKIP:
            self.description = description 

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
        code = dictionary.get("Code") if dictionary.get("Code") else APIHelper.SKIP
        description = dictionary.get("Description") if dictionary.get("Description") else APIHelper.SKIP
        # Return an object of this model
        return cls(code,
                   description)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'code={(self.code if hasattr(self, "code") else None)!r}, '
                f'description={(self.description if hasattr(self, "description") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'code={(self.code if hasattr(self, "code") else None)!s}, '
                f'description={(self.description if hasattr(self, "description") else None)!s})')
