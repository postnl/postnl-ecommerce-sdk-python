# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""


class ProductOption(object):

    """Implementation of the 'ProductOption' model.

    Attributes:
        characteristic (str): The characteristic of the ProductOption.
            Mandatory for some products, please see the [Products
            page](https://developer.postnl.nl/docs/#/http/reference-data/produc
            t-codes-dutch-domestic)
        option (str): The product option code for this ProductOption.
            Mandatory for some products, please see the [Products
            page](https://developer.postnl.nl/docs/#/http/reference-data/produc
            t-codes-dutch-domestic)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "characteristic": 'Characteristic',
        "option": 'Option'
    }

    def __init__(self,
                 characteristic='118',
                 option='006'):
        """Constructor for the ProductOption class"""

        # Initialize members of the class
        self.characteristic = characteristic 
        self.option = option 

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
        characteristic = dictionary.get("Characteristic") if dictionary.get("Characteristic") else '118'
        option = dictionary.get("Option") if dictionary.get("Option") else '006'
        # Return an object of this model
        return cls(characteristic,
                   option)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'characteristic={self.characteristic!r}, '
                f'option={self.option!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'characteristic={self.characteristic!s}, '
                f'option={self.option!s})')
