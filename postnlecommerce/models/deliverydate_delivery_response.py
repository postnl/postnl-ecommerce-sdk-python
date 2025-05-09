# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper
from postnlecommerce.models.deliverydate_options import DeliverydateOptions
from postnlecommerce.models.sustainability import Sustainability


class DeliverydateDeliveryResponse(object):

    """Implementation of the 'deliverydateDeliveryResponse' model.

    Attributes:
        delivery_date (str): The model property of type str.
        options (DeliverydateOptions): The delivery options for which a
            delivery date is returned. Only one delivery option is specified.
            See [Delivery
            Options](https://developer.postnl.nl/docs/#/http/reference-data/ref
            erence-codes/delivery-options) for possible values.
        sustainability (Sustainability): Sustainability score; see
            [Sustainability
            codes](https://developer.postnl.nl/docs/#/http/reference-data/refer
            ence-codes/sustainability-codes) for possible values.

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
        """Constructor for the DeliverydateDeliveryResponse class"""

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

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        delivery_date = dictionary.get("DeliveryDate") if dictionary.get("DeliveryDate") else APIHelper.SKIP
        options = DeliverydateOptions.from_dictionary(dictionary.get('Options')) if 'Options' in dictionary.keys() else APIHelper.SKIP
        sustainability = Sustainability.from_dictionary(dictionary.get('Sustainability')) if 'Sustainability' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(delivery_date,
                   options,
                   sustainability)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'delivery_date={(self.delivery_date if hasattr(self, "delivery_date") else None)!r}, '
                f'options={(self.options if hasattr(self, "options") else None)!r}, '
                f'sustainability={(self.sustainability if hasattr(self, "sustainability") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'delivery_date={(self.delivery_date if hasattr(self, "delivery_date") else None)!s}, '
                f'options={(self.options if hasattr(self, "options") else None)!s}, '
                f'sustainability={(self.sustainability if hasattr(self, "sustainability") else None)!s})')
