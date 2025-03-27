# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper
from postnlecommerce.models.complete_status_shipment import CompleteStatusShipment


class CompleteStatus(object):

    """Implementation of the 'CompleteStatus' model.

    The current status and old statuses of the shipment

    Attributes:
        shipment (CompleteStatusShipment): The model property of type
            CompleteStatusShipment.

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
        """Constructor for the CompleteStatus class"""

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

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        shipment = CompleteStatusShipment.from_dictionary(dictionary.get('Shipment')) if 'Shipment' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(shipment)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'shipment={(self.shipment if hasattr(self, "shipment") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'shipment={(self.shipment if hasattr(self, "shipment") else None)!s})')
