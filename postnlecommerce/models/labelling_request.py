# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper
from postnlecommerce.models.labelling_customer import LabellingCustomer
from postnlecommerce.models.labelling_customer_message import LabellingCustomerMessage
from postnlecommerce.models.labelling_customer_shipment import LabellingCustomerShipment


class LabellingRequest(object):

    """Implementation of the 'labellingRequest' model.

    TODO: type model description here.

    Attributes:
        customer (LabellingCustomer): TODO: type description here.
        label_signature (str): GIF image of the signature (as a base64 encoded
            string) max size: 280x60 mm (1058x226 pixels). This can be used to
            automatically sign the customs forms. The value of this element
            can have a maximum size of 65536 characters. Note that the total
            request can have a maximum size of 200KB. Larger requests will not
            be accepted by the server for performance reasons. Requests that
            exceed this limit will not return a validation error,but a HTTP
            404 error.
        message (LabellingCustomerMessage): TODO: type description here.
        shipments (List[LabellingCustomerShipment]): List of 1 or more
            Shipments. At least 1 shipment is required.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "customer": 'Customer',
        "message": 'Message',
        "shipments": 'Shipments',
        "label_signature": 'LabelSignature'
    }

    _optionals = [
        'label_signature',
    ]

    def __init__(self,
                 customer=None,
                 message=None,
                 shipments=None,
                 label_signature=APIHelper.SKIP):
        """Constructor for the LabellingRequest class"""

        # Initialize members of the class
        self.customer = customer 
        if label_signature is not APIHelper.SKIP:
            self.label_signature = label_signature 
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
        customer = LabellingCustomer.from_dictionary(dictionary.get('Customer')) if dictionary.get('Customer') else None
        message = LabellingCustomerMessage.from_dictionary(dictionary.get('Message')) if dictionary.get('Message') else None
        shipments = None
        if dictionary.get('Shipments') is not None:
            shipments = [LabellingCustomerShipment.from_dictionary(x) for x in dictionary.get('Shipments')]
        label_signature = dictionary.get("LabelSignature") if dictionary.get("LabelSignature") else APIHelper.SKIP
        # Return an object of this model
        return cls(customer,
                   message,
                   shipments,
                   label_signature)
