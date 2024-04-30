# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper


class Amount1(object):

    """Implementation of the 'Amount1' model.

    The amounts belonging to the shipment

    Attributes:
        rembours_bedrag (str): The cash-on-delivery (COD) amount
        verzekerd_bedrag (str): The insurance amount of the shipment

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "rembours_bedrag": 'RemboursBedrag',
        "verzekerd_bedrag": 'VerzekerdBedrag'
    }

    _optionals = [
        'rembours_bedrag',
        'verzekerd_bedrag',
    ]

    def __init__(self,
                 rembours_bedrag=APIHelper.SKIP,
                 verzekerd_bedrag=APIHelper.SKIP):
        """Constructor for the Amount1 class"""

        # Initialize members of the class
        if rembours_bedrag is not APIHelper.SKIP:
            self.rembours_bedrag = rembours_bedrag 
        if verzekerd_bedrag is not APIHelper.SKIP:
            self.verzekerd_bedrag = verzekerd_bedrag 

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
        rembours_bedrag = dictionary.get("RemboursBedrag") if dictionary.get("RemboursBedrag") else APIHelper.SKIP
        verzekerd_bedrag = dictionary.get("VerzekerdBedrag") if dictionary.get("VerzekerdBedrag") else APIHelper.SKIP
        # Return an object of this model
        return cls(rembours_bedrag,
                   verzekerd_bedrag)
