# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper


class BarcodeResponse(object):

    """Implementation of the 'barcodeResponse' model.

    Attributes:
        barcode (str): The model property of type str.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "barcode": 'Barcode'
    }

    _optionals = [
        'barcode',
    ]

    def __init__(self,
                 barcode=APIHelper.SKIP):
        """Constructor for the BarcodeResponse class"""

        # Initialize members of the class
        if barcode is not APIHelper.SKIP:
            self.barcode = barcode 

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
        barcode = dictionary.get("Barcode") if dictionary.get("Barcode") else APIHelper.SKIP
        # Return an object of this model
        return cls(barcode)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'barcode={(self.barcode if hasattr(self, "barcode") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'barcode={(self.barcode if hasattr(self, "barcode") else None)!s})')
