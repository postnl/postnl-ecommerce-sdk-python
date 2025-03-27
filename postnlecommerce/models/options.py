# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper


class Options(object):

    """Implementation of the 'Options' model.

    The delivery option for which the timeframe is calculated. See [Delivery
    Options](https://developer.postnl.nl/docs/#/http/reference-data/reference-c
    odes/delivery-options) for possible values.

    Attributes:
        string (TimeframeOptionsEnum): The model property of type
            TimeframeOptionsEnum.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "string": 'string'
    }

    _optionals = [
        'string',
    ]

    def __init__(self,
                 string=APIHelper.SKIP):
        """Constructor for the Options class"""

        # Initialize members of the class
        if string is not APIHelper.SKIP:
            self.string = string 

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
        string = dictionary.get("string") if dictionary.get("string") else APIHelper.SKIP
        # Return an object of this model
        return cls(string)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'string={(self.string if hasattr(self, "string") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'string={(self.string if hasattr(self, "string") else None)!s})')
