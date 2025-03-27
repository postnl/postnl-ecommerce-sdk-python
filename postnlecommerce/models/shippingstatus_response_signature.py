# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper
from postnlecommerce.models.signature import Signature
from postnlecommerce.models.warnings import Warnings


class ShippingstatusResponseSignature(object):

    """Implementation of the 'shippingstatusResponseSignature' model.

    Attributes:
        signature (Signature): The model property of type Signature.
        warnings (Warnings): The model property of type Warnings.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "signature": 'Signature',
        "warnings": 'Warnings'
    }

    _optionals = [
        'signature',
        'warnings',
    ]

    def __init__(self,
                 signature=APIHelper.SKIP,
                 warnings=APIHelper.SKIP):
        """Constructor for the ShippingstatusResponseSignature class"""

        # Initialize members of the class
        if signature is not APIHelper.SKIP:
            self.signature = signature 
        if warnings is not APIHelper.SKIP:
            self.warnings = warnings 

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
        signature = Signature.from_dictionary(dictionary.get('Signature')) if 'Signature' in dictionary.keys() else APIHelper.SKIP
        warnings = Warnings.from_dictionary(dictionary.get('Warnings')) if 'Warnings' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(signature,
                   warnings)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'signature={(self.signature if hasattr(self, "signature") else None)!r}, '
                f'warnings={(self.warnings if hasattr(self, "warnings") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'signature={(self.signature if hasattr(self, "signature") else None)!s}, '
                f'warnings={(self.warnings if hasattr(self, "warnings") else None)!s})')
