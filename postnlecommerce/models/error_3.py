# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper


class Error3(object):

    """Implementation of the 'Error3' model.

    TODO: type model description here.

    Attributes:
        error (str): The error reason
        code (str): The error code
        description (str): The description of the error

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "error": 'Error',
        "code": 'Code',
        "description": 'Description'
    }

    _optionals = [
        'error',
        'code',
        'description',
    ]

    def __init__(self,
                 error=APIHelper.SKIP,
                 code=APIHelper.SKIP,
                 description=APIHelper.SKIP):
        """Constructor for the Error3 class"""

        # Initialize members of the class
        if error is not APIHelper.SKIP:
            self.error = error 
        if code is not APIHelper.SKIP:
            self.code = code 
        if description is not APIHelper.SKIP:
            self.description = description 

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
        error = dictionary.get("Error") if dictionary.get("Error") else APIHelper.SKIP
        code = dictionary.get("Code") if dictionary.get("Code") else APIHelper.SKIP
        description = dictionary.get("Description") if dictionary.get("Description") else APIHelper.SKIP
        # Return an object of this model
        return cls(error,
                   code,
                   description)
