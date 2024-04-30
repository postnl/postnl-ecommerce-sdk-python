# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper
from postnlecommerce.models.product_option_1 import ProductOption1


class ProductOptions(object):

    """Implementation of the 'ProductOptions' model.

    A list of product options.

    Attributes:
        product_option (ProductOption1): TODO: type description here.

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
        """Constructor for the ProductOptions class"""

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

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        product_option = ProductOption1.from_dictionary(dictionary.get('ProductOption')) if 'ProductOption' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(product_option)
