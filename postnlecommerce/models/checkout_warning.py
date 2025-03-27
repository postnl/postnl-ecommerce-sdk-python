# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper


class CheckoutWarning(object):

    """Implementation of the 'checkoutWarning' model.

    Attributes:
        delivery_date (str): Deliverydate that triggered the warning
        code (str): Warning code (for a possible list of warnings, see the
            generic error codes page)
        description (str): Warning description (for a possible list of
            warnings, see the generic error codes page)
        options (CheckoutWarningOptionEnum): The model property of type
            CheckoutWarningOptionEnum.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "delivery_date": 'DeliveryDate',
        "code": 'Code',
        "description": 'Description',
        "options": 'Options'
    }

    _optionals = [
        'delivery_date',
        'code',
        'description',
        'options',
    ]

    def __init__(self,
                 delivery_date=APIHelper.SKIP,
                 code=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 options=APIHelper.SKIP):
        """Constructor for the CheckoutWarning class"""

        # Initialize members of the class
        if delivery_date is not APIHelper.SKIP:
            self.delivery_date = delivery_date 
        if code is not APIHelper.SKIP:
            self.code = code 
        if description is not APIHelper.SKIP:
            self.description = description 
        if options is not APIHelper.SKIP:
            self.options = options 

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
        code = dictionary.get("Code") if dictionary.get("Code") else APIHelper.SKIP
        description = dictionary.get("Description") if dictionary.get("Description") else APIHelper.SKIP
        options = dictionary.get("Options") if dictionary.get("Options") else APIHelper.SKIP
        # Return an object of this model
        return cls(delivery_date,
                   code,
                   description,
                   options)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'delivery_date={(self.delivery_date if hasattr(self, "delivery_date") else None)!r}, '
                f'code={(self.code if hasattr(self, "code") else None)!r}, '
                f'description={(self.description if hasattr(self, "description") else None)!r}, '
                f'options={(self.options if hasattr(self, "options") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'delivery_date={(self.delivery_date if hasattr(self, "delivery_date") else None)!s}, '
                f'code={(self.code if hasattr(self, "code") else None)!s}, '
                f'description={(self.description if hasattr(self, "description") else None)!s}, '
                f'options={(self.options if hasattr(self, "options") else None)!s})')
