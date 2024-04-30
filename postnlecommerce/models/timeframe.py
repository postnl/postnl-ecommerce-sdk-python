# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper
from postnlecommerce.models.sustainability import Sustainability


class Timeframe(object):

    """Implementation of the 'Timeframe' model.

    TODO: type model description here.

    Attributes:
        mfrom (str): Format hh:mm:ss
        to (str): Format hh:mm:ss
        options (List[Option1Enum]): The delivery options applicable to the
            timeframe information. See [Delivery
            Options](#tag/Reference-codes/Delivery-options) for possible
            values.
        shipping_date (str): The date when you need to deliver the shipment to
            PostNL to ensure the expected delivery date is achieved. Will be
            returned as 'null' if not calculated
        sustainability (Sustainability): Sustainability score; see
            [Sustainability codes](#tag/Reference-codes/Sustainability-codes)
            for possible values.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mfrom": 'From',
        "to": 'To',
        "options": 'Options',
        "shipping_date": 'ShippingDate',
        "sustainability": 'Sustainability'
    }

    _optionals = [
        'mfrom',
        'to',
        'options',
        'shipping_date',
        'sustainability',
    ]

    def __init__(self,
                 mfrom=APIHelper.SKIP,
                 to=APIHelper.SKIP,
                 options=APIHelper.SKIP,
                 shipping_date=APIHelper.SKIP,
                 sustainability=APIHelper.SKIP):
        """Constructor for the Timeframe class"""

        # Initialize members of the class
        if mfrom is not APIHelper.SKIP:
            self.mfrom = mfrom 
        if to is not APIHelper.SKIP:
            self.to = to 
        if options is not APIHelper.SKIP:
            self.options = options 
        if shipping_date is not APIHelper.SKIP:
            self.shipping_date = shipping_date 
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
        mfrom = dictionary.get("From") if dictionary.get("From") else APIHelper.SKIP
        to = dictionary.get("To") if dictionary.get("To") else APIHelper.SKIP
        options = dictionary.get("Options") if dictionary.get("Options") else APIHelper.SKIP
        shipping_date = dictionary.get("ShippingDate") if dictionary.get("ShippingDate") else APIHelper.SKIP
        sustainability = Sustainability.from_dictionary(dictionary.get('Sustainability')) if 'Sustainability' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(mfrom,
                   to,
                   options,
                   shipping_date,
                   sustainability)
