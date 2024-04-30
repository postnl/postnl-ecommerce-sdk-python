# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper
from postnlecommerce.models.shipment_11 import Shipment11


class CurrentStatus(object):

    """Implementation of the 'CurrentStatus' model.

    The current status and old statuses of the shipment

    Attributes:
        shipment (List[Shipment11]): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "shipment": 'Shipment'
    }

    _optionals = [
        'shipment',
    ]

    def __init__(self,
                 shipment=APIHelper.SKIP):
        """Constructor for the CurrentStatus class"""

        # Initialize members of the class
        if shipment is not APIHelper.SKIP:
            self.shipment = shipment 

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
        shipment = None
        if dictionary.get('Shipment') is not None:
            shipment = [Shipment11.from_dictionary(x) for x in dictionary.get('Shipment')]
        else:
            shipment = APIHelper.SKIP
        # Return an object of this model
        return cls(shipment)
