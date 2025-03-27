# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper


class Detail(object):

    """Implementation of the 'Detail' model.

    Attributes:
        errorcode (str): The model property of type str.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "errorcode": 'errorcode'
    }

    _optionals = [
        'errorcode',
    ]

    def __init__(self,
                 errorcode=APIHelper.SKIP):
        """Constructor for the Detail class"""

        # Initialize members of the class
        if errorcode is not APIHelper.SKIP:
            self.errorcode = errorcode 

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
        errorcode = dictionary.get("errorcode") if dictionary.get("errorcode") else APIHelper.SKIP
        # Return an object of this model
        return cls(errorcode)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'errorcode={(self.errorcode if hasattr(self, "errorcode") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'errorcode={(self.errorcode if hasattr(self, "errorcode") else None)!s})')
