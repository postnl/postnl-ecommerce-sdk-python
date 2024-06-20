# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.models.confirming_message import ConfirmingMessage
from postnlecommerce.models.confirming_shipment import ConfirmingShipment
from postnlecommerce.models.customer import Customer


class ConfirmingRequest(object):

    """Implementation of the 'confirmingRequest' model.

    TODO: type model description here.

    Attributes:
        customer (Customer): TODO: type description here.
        message (ConfirmingMessage): TODO: type description here.
        shipments (List[ConfirmingShipment]): List of 1 or more Shipments. At
            least 1 shipment is required.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "customer": 'Customer',
        "message": 'Message',
        "shipments": 'Shipments'
    }

    def __init__(self,
                 customer=None,
                 message=None,
                 shipments=None):
        """Constructor for the ConfirmingRequest class"""

        # Initialize members of the class
        self.customer = customer 
        self.message = message 
        self.shipments = shipments 

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
        customer = Customer.from_dictionary(dictionary.get('Customer')) if dictionary.get('Customer') else None
        message = ConfirmingMessage.from_dictionary(dictionary.get('Message')) if dictionary.get('Message') else None
        shipments = None
        if dictionary.get('Shipments') is not None:
            shipments = [ConfirmingShipment.from_dictionary(x) for x in dictionary.get('Shipments')]
        # Return an object of this model
        return cls(customer,
                   message,
                   shipments)
