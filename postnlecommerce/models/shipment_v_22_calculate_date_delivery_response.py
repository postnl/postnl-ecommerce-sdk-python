# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper
from postnlecommerce.models.options import Options
from postnlecommerce.models.warning_1 import Warning1


class ShipmentV22CalculateDateDeliveryResponse(object):

    """Implementation of the 'Shipment V2 2 Calculate Date Delivery Response' model.

    TODO: type model description here.

    Attributes:
        delivery_date (str): TODO: type description here.
        options (Options): The delivery options for which a delivery date is
            returned. Only one delivery option is specified. See [Delivery
            Options](#tag/Reference-codes/Delivery-options) for possible
            values.
        sustainability (Warning1): Sustainability score; see [Sustainability
            codes](#tag/Reference-codes/Sustainability-codes) for possible
            values.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "delivery_date": 'DeliveryDate',
        "options": 'Options',
        "sustainability": 'Sustainability'
    }

    _optionals = [
        'delivery_date',
        'options',
        'sustainability',
    ]

    def __init__(self,
                 delivery_date=APIHelper.SKIP,
                 options=APIHelper.SKIP,
                 sustainability=APIHelper.SKIP):
        """Constructor for the ShipmentV22CalculateDateDeliveryResponse class"""

        # Initialize members of the class
        if delivery_date is not APIHelper.SKIP:
            self.delivery_date = delivery_date 
        if options is not APIHelper.SKIP:
            self.options = options 
        if sustainability is not APIHelper.SKIP:
            self.sustainability = sustainability 

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
        delivery_date = dictionary.get("DeliveryDate") if dictionary.get("DeliveryDate") else APIHelper.SKIP
        options = Options.from_dictionary(dictionary.get('Options')) if 'Options' in dictionary.keys() else APIHelper.SKIP
        sustainability = Warning1.from_dictionary(dictionary.get('Sustainability')) if 'Sustainability' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(delivery_date,
                   options,
                   sustainability)
