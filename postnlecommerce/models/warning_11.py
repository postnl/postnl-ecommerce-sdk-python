# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper


class Warning11(object):

    """Implementation of the 'Warning11' model.

    TODO: type model description here.

    Attributes:
        message (str): Warning message
        code (str): Warning code

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "message": 'Message',
        "code": 'Code'
    }

    _optionals = [
        'message',
        'code',
    ]

    def __init__(self,
                 message=APIHelper.SKIP,
                 code=APIHelper.SKIP):
        """Constructor for the Warning11 class"""

        # Initialize members of the class
        if message is not APIHelper.SKIP:
            self.message = message 
        if code is not APIHelper.SKIP:
            self.code = code 

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
        message = dictionary.get("Message") if dictionary.get("Message") else APIHelper.SKIP
        code = dictionary.get("Code") if dictionary.get("Code") else APIHelper.SKIP
        # Return an object of this model
        return cls(message,
                   code)
