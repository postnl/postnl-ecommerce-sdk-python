# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper


class Warning(object):

    """Implementation of the 'Warning' model.

    TODO: type model description here.

    Attributes:
        delivery_date (str): Deliverydate that triggered the warning
        code (str): Warning code (for a possible list of warnings, see the
            generic error codes page)
        description (str): Warning description (for a possible list of
            warnings, see the generic error codes page)
        options (List[Option2Enum]): The option that triggered the warning

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
        """Constructor for the Warning class"""

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

        if dictionary is None:
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
