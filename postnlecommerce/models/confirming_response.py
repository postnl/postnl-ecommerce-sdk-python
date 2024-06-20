# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper
from postnlecommerce.models.confirming_response_shipment import ConfirmingResponseShipment


class ConfirmingResponse(object):

    """Implementation of the 'confirmingResponse' model.

    TODO: type model description here.

    Attributes:
        response_shipments (List[ConfirmingResponseShipment]): TODO: type
            description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "response_shipments": 'ResponseShipments'
    }

    _optionals = [
        'response_shipments',
    ]

    def __init__(self,
                 response_shipments=APIHelper.SKIP):
        """Constructor for the ConfirmingResponse class"""

        # Initialize members of the class
        if response_shipments is not APIHelper.SKIP:
            self.response_shipments = response_shipments 

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
        response_shipments = None
        if dictionary.get('ResponseShipments') is not None:
            response_shipments = [ConfirmingResponseShipment.from_dictionary(x) for x in dictionary.get('ResponseShipments')]
        else:
            response_shipments = APIHelper.SKIP
        # Return an object of this model
        return cls(response_shipments)
