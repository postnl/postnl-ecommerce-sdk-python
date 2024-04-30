# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper


class Friday(object):

    """Implementation of the 'Friday' model.

    TODO: type model description here.

    Attributes:
        mfrom (str): TODO: type description here.
        to (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mfrom": 'From',
        "to": 'To'
    }

    _optionals = [
        'mfrom',
        'to',
    ]

    def __init__(self,
                 mfrom=APIHelper.SKIP,
                 to=APIHelper.SKIP):
        """Constructor for the Friday class"""

        # Initialize members of the class
        if mfrom is not APIHelper.SKIP:
            self.mfrom = mfrom 
        if to is not APIHelper.SKIP:
            self.to = to 

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
        mfrom = dictionary.get("From") if dictionary.get("From") else APIHelper.SKIP
        to = dictionary.get("To") if dictionary.get("To") else APIHelper.SKIP
        # Return an object of this model
        return cls(mfrom,
                   to)
