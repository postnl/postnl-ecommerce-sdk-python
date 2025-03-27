# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper
from postnlecommerce.models.sustainability import Sustainability


class CheckoutTimeFrame(object):

    """Implementation of the 'checkoutTimeFrame' model.

    Attributes:
        mfrom (str): Format hh:mm:ss
        to (str): Format hh:mm:ss
        options (List[CheckoutOptionEnum]): The delivery options applicable to
            the timeframe information. See [Delivery
            Options](https://developer.postnl.nl/docs/#/http/reference-data/ref
            erence-codes/delivery-options) for possible values.
        shipping_date (str): The date when you need to deliver the shipment to
            PostNL to ensure the expected delivery date is achieved. Will be
            returned as 'null' if not calculated
        sustainability (Sustainability): Sustainability score; see
            [Sustainability
            codes](https://developer.postnl.nl/docs/#/http/reference-data/refer
            ence-codes/sustainability-codes) for possible values.

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
        """Constructor for the CheckoutTimeFrame class"""

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

        if not isinstance(dictionary, dict) or dictionary is None:
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

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'mfrom={(self.mfrom if hasattr(self, "mfrom") else None)!r}, '
                f'to={(self.to if hasattr(self, "to") else None)!r}, '
                f'options={(self.options if hasattr(self, "options") else None)!r}, '
                f'shipping_date={(self.shipping_date if hasattr(self, "shipping_date") else None)!r}, '
                f'sustainability={(self.sustainability if hasattr(self, "sustainability") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'mfrom={(self.mfrom if hasattr(self, "mfrom") else None)!s}, '
                f'to={(self.to if hasattr(self, "to") else None)!s}, '
                f'options={(self.options if hasattr(self, "options") else None)!s}, '
                f'shipping_date={(self.shipping_date if hasattr(self, "shipping_date") else None)!s}, '
                f'sustainability={(self.sustainability if hasattr(self, "sustainability") else None)!s})')
