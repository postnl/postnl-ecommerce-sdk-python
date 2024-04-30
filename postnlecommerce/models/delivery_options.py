# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper


class DeliveryOptions(object):

    """Implementation of the 'DeliveryOptions' model.

    The options belonging to the pickup location. The delivery options RETA,
    UL, PU, DO, BW, RT and BWUL can be shown in the response. Please ignore
    these codes. These codes are internal PostNL codes.

    Attributes:
        string (List[str]): TODO: type description here.

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
        """Constructor for the DeliveryOptions class"""

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

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        string = dictionary.get("string") if dictionary.get("string") else APIHelper.SKIP
        # Return an object of this model
        return cls(string)
