# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper


class Error4(object):

    """Implementation of the 'Error4' model.

    TODO: type model description here.

    Attributes:
        status (str): TODO: type description here.
        title (str): TODO: type description here.
        detail (str): TODO: type description here.

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
        """Constructor for the Error4 class"""

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

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        status = dictionary.get("status") if dictionary.get("status") else APIHelper.SKIP
        title = dictionary.get("title") if dictionary.get("title") else APIHelper.SKIP
        detail = dictionary.get("detail") if dictionary.get("detail") else APIHelper.SKIP
        # Return an object of this model
        return cls(status,
                   title,
                   detail)
