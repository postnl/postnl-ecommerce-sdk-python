# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper


class ShipmentV22CalculateDateShippingResponse(object):

    """Implementation of the 'Shipment V2 2 Calculate Date Shipping Response' model.

    TODO: type model description here.

    Attributes:
        sent_date (str): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "sent_date": 'SentDate'
    }

    _optionals = [
        'sent_date',
    ]

    def __init__(self,
                 sent_date=APIHelper.SKIP):
        """Constructor for the ShipmentV22CalculateDateShippingResponse class"""

        # Initialize members of the class
        if sent_date is not APIHelper.SKIP:
            self.sent_date = sent_date 

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
        sent_date = dictionary.get("SentDate") if dictionary.get("SentDate") else APIHelper.SKIP
        # Return an object of this model
        return cls(sent_date)
