# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper


class Expectation(object):

    """Implementation of the 'Expectation' model.

    The expected delivery timeframe

    Attributes:
        eta_from (str): The start of the timeframe
        eta_to (str): The end of the timeframe

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "eta_from": 'ETAFrom',
        "eta_to": 'ETATo'
    }

    _optionals = [
        'eta_from',
        'eta_to',
    ]

    def __init__(self,
                 eta_from=APIHelper.SKIP,
                 eta_to=APIHelper.SKIP):
        """Constructor for the Expectation class"""

        # Initialize members of the class
        if eta_from is not APIHelper.SKIP:
            self.eta_from = eta_from 
        if eta_to is not APIHelper.SKIP:
            self.eta_to = eta_to 

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
        eta_from = dictionary.get("ETAFrom") if dictionary.get("ETAFrom") else APIHelper.SKIP
        eta_to = dictionary.get("ETATo") if dictionary.get("ETATo") else APIHelper.SKIP
        # Return an object of this model
        return cls(eta_from,
                   eta_to)
