# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper
from postnlecommerce.models.detail import Detail


class Fault(object):

    """Implementation of the 'Fault' model.

    Attributes:
        faultstring (str): The model property of type str.
        detail (Detail): The model property of type Detail.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "faultstring": 'faultstring',
        "detail": 'detail'
    }

    _optionals = [
        'faultstring',
        'detail',
    ]

    def __init__(self,
                 faultstring=APIHelper.SKIP,
                 detail=APIHelper.SKIP):
        """Constructor for the Fault class"""

        # Initialize members of the class
        if faultstring is not APIHelper.SKIP:
            self.faultstring = faultstring 
        if detail is not APIHelper.SKIP:
            self.detail = detail 

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
        faultstring = dictionary.get("faultstring") if dictionary.get("faultstring") else APIHelper.SKIP
        detail = Detail.from_dictionary(dictionary.get('detail')) if 'detail' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(faultstring,
                   detail)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'faultstring={(self.faultstring if hasattr(self, "faultstring") else None)!r}, '
                f'detail={(self.detail if hasattr(self, "detail") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'faultstring={(self.faultstring if hasattr(self, "faultstring") else None)!s}, '
                f'detail={(self.detail if hasattr(self, "detail") else None)!s})')
