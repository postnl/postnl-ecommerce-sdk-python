# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper


class DeliverydateShippingResponse(object):

    """Implementation of the 'deliverydateShippingResponse' model.

    Attributes:
        sent_date (str): The model property of type str.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "sent_date": 'SentDate'
    }

    _optionals = [
        'sent_date',
    ]

    def __init__(self,
                 sent_date=APIHelper.SKIP):
        """Constructor for the DeliverydateShippingResponse class"""

        # Initialize members of the class
        if sent_date is not APIHelper.SKIP:
            self.sent_date = sent_date 

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
        sent_date = dictionary.get("SentDate") if dictionary.get("SentDate") else APIHelper.SKIP
        # Return an object of this model
        return cls(sent_date)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'sent_date={(self.sent_date if hasattr(self, "sent_date") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'sent_date={(self.sent_date if hasattr(self, "sent_date") else None)!s})')
