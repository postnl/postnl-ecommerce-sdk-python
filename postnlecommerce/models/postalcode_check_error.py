# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper


class PostalcodeCheckError(object):

    """Implementation of the 'postalcodeCheckError' model.

    Attributes:
        status (str): The model property of type str.
        title (str): The model property of type str.
        detail (str): The model property of type str.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "status": 'status',
        "title": 'title',
        "detail": 'detail'
    }

    _optionals = [
        'status',
        'title',
        'detail',
    ]

    def __init__(self,
                 status=APIHelper.SKIP,
                 title=APIHelper.SKIP,
                 detail=APIHelper.SKIP):
        """Constructor for the PostalcodeCheckError class"""

        # Initialize members of the class
        if status is not APIHelper.SKIP:
            self.status = status 
        if title is not APIHelper.SKIP:
            self.title = title 
        if detail is not APIHelper.SKIP:
            self.detail = detail 

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
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        title = dictionary.get("title") if dictionary.get("title") else APIHelper.SKIP
        detail = dictionary.get("detail") if dictionary.get("detail") else APIHelper.SKIP
        # Return an object of this model
        return cls(status,
                   title,
                   detail)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'status={(self.status if hasattr(self, "status") else None)!r}, '
                f'title={(self.title if hasattr(self, "title") else None)!r}, '
                f'detail={(self.detail if hasattr(self, "detail") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'status={(self.status if hasattr(self, "status") else None)!s}, '
                f'title={(self.title if hasattr(self, "title") else None)!s}, '
                f'detail={(self.detail if hasattr(self, "detail") else None)!s})')
