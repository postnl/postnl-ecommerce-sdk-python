# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper


class Detail(object):

    """Implementation of the 'Detail' model.

    TODO: type model description here.

    Attributes:
        errorcode (str): TODO: type description here.

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

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        errorcode = dictionary.get("errorcode") if dictionary.get("errorcode") else APIHelper.SKIP
        # Return an object of this model
        return cls(errorcode)
