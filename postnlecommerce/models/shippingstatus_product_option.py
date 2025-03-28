# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper


class ShippingstatusProductOption(object):

    """Implementation of the 'shippingstatusProductOption' model.

    Attributes:
        option_code (str): The product option code for this ProductOption.
        characteristic_code (str): The characteristic of the ProductOption.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "option_code": 'OptionCode',
        "characteristic_code": 'CharacteristicCode'
    }

    _optionals = [
        'option_code',
        'characteristic_code',
    ]

    def __init__(self,
                 option_code=APIHelper.SKIP,
                 characteristic_code=APIHelper.SKIP):
        """Constructor for the ShippingstatusProductOption class"""

        # Initialize members of the class
        if option_code is not APIHelper.SKIP:
            self.option_code = option_code 
        if characteristic_code is not APIHelper.SKIP:
            self.characteristic_code = characteristic_code 

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
        option_code = dictionary.get("OptionCode") if dictionary.get("OptionCode") else APIHelper.SKIP
        characteristic_code = dictionary.get("CharacteristicCode") if dictionary.get("CharacteristicCode") else APIHelper.SKIP
        # Return an object of this model
        return cls(option_code,
                   characteristic_code)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'option_code={(self.option_code if hasattr(self, "option_code") else None)!r}, '
                f'characteristic_code={(self.characteristic_code if hasattr(self, "characteristic_code") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'option_code={(self.option_code if hasattr(self, "option_code") else None)!s}, '
                f'characteristic_code={(self.characteristic_code if hasattr(self, "characteristic_code") else None)!s})')
