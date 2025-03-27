# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper
from postnlecommerce.models.shippingstatus_product_option import ShippingstatusProductOption


class ShippingstatusProductOptions(object):

    """Implementation of the 'shippingstatusProductOptions' model.

    Attributes:
        product_option (ShippingstatusProductOption): The model property of
            type ShippingstatusProductOption.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "product_option": 'ProductOption'
    }

    _optionals = [
        'product_option',
    ]

    def __init__(self,
                 product_option=APIHelper.SKIP):
        """Constructor for the ShippingstatusProductOptions class"""

        # Initialize members of the class
        if product_option is not APIHelper.SKIP:
            self.product_option = product_option 

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
        product_option = ShippingstatusProductOption.from_dictionary(dictionary.get('ProductOption')) if 'ProductOption' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(product_option)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'product_option={(self.product_option if hasattr(self, "product_option") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'product_option={(self.product_option if hasattr(self, "product_option") else None)!s})')
