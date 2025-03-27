# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper


class ExtraField(object):

    """Implementation of the 'ExtraField' model.

    Attributes:
        key (str): The model property of type str.
        value (str): The model property of type str.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "key": 'Key',
        "value": 'Value'
    }

    _optionals = [
        'key',
        'value',
    ]

    def __init__(self,
                 key=APIHelper.SKIP,
                 value=APIHelper.SKIP):
        """Constructor for the ExtraField class"""

        # Initialize members of the class
        if key is not APIHelper.SKIP:
            self.key = key 
        if value is not APIHelper.SKIP:
            self.value = value 

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
        key = dictionary.get("Key") if dictionary.get("Key") else APIHelper.SKIP
        value = dictionary.get("Value") if dictionary.get("Value") else APIHelper.SKIP
        # Return an object of this model
        return cls(key,
                   value)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'key={(self.key if hasattr(self, "key") else None)!r}, '
                f'value={(self.value if hasattr(self, "value") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'key={(self.key if hasattr(self, "key") else None)!s}, '
                f'value={(self.value if hasattr(self, "value") else None)!s})')
