# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper
from postnlecommerce.models.confirming_error import ConfirmingError
from postnlecommerce.models.warning import Warning


class ConfirmingResponseShipment(object):

    """Implementation of the 'confirmingResponseShipment' model.

    Attributes:
        errors (List[ConfirmingError]): Possible errors. See the [Error
            Codes](https://developer.postnl.nl/docs/#/http/reference-data/error
            -codes) for possible values
        warnings (List[Warning]): Possible warnings. See the [Error
            Codes](https://developer.postnl.nl/docs/#/http/reference-data/error
            -codes) for possible values
        barcode (str): The barcode used

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "errors": 'Errors',
        "warnings": 'Warnings',
        "barcode": 'Barcode'
    }

    _optionals = [
        'errors',
        'warnings',
        'barcode',
    ]

    def __init__(self,
                 errors=APIHelper.SKIP,
                 warnings=APIHelper.SKIP,
                 barcode=APIHelper.SKIP):
        """Constructor for the ConfirmingResponseShipment class"""

        # Initialize members of the class
        if errors is not APIHelper.SKIP:
            self.errors = errors 
        if warnings is not APIHelper.SKIP:
            self.warnings = warnings 
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
        errors = None
        if dictionary.get('Errors') is not None:
            errors = [ConfirmingError.from_dictionary(x) for x in dictionary.get('Errors')]
        else:
            errors = APIHelper.SKIP
        warnings = None
        if dictionary.get('Warnings') is not None:
            warnings = [Warning.from_dictionary(x) for x in dictionary.get('Warnings')]
        else:
            warnings = APIHelper.SKIP
        barcode = dictionary.get("Barcode") if dictionary.get("Barcode") else APIHelper.SKIP
        # Return an object of this model
        return cls(errors,
                   warnings,
                   barcode)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'errors={(self.errors if hasattr(self, "errors") else None)!r}, '
                f'warnings={(self.warnings if hasattr(self, "warnings") else None)!r}, '
                f'barcode={(self.barcode if hasattr(self, "barcode") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'errors={(self.errors if hasattr(self, "errors") else None)!s}, '
                f'warnings={(self.warnings if hasattr(self, "warnings") else None)!s}, '
                f'barcode={(self.barcode if hasattr(self, "barcode") else None)!s})')
