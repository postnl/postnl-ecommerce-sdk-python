# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper


class Customer2(object):

    """Implementation of the 'Customer2' model.

    TODO: type model description here.

    Attributes:
        customer_code (str): The customer code of the shipment
        customer_number (str): The customer number of the shipment
        name (str): The customer name

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "customer_code": 'CustomerCode',
        "customer_number": 'CustomerNumber',
        "name": 'Name'
    }

    _optionals = [
        'customer_code',
        'customer_number',
        'name',
    ]

    def __init__(self,
                 customer_code=APIHelper.SKIP,
                 customer_number=APIHelper.SKIP,
                 name=APIHelper.SKIP):
        """Constructor for the Customer2 class"""

        # Initialize members of the class
        if customer_code is not APIHelper.SKIP:
            self.customer_code = customer_code 
        if customer_number is not APIHelper.SKIP:
            self.customer_number = customer_number 
        if name is not APIHelper.SKIP:
            self.name = name 

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
        customer_code = dictionary.get("CustomerCode") if dictionary.get("CustomerCode") else APIHelper.SKIP
        customer_number = dictionary.get("CustomerNumber") if dictionary.get("CustomerNumber") else APIHelper.SKIP
        name = dictionary.get("Name") if dictionary.get("Name") else APIHelper.SKIP
        # Return an object of this model
        return cls(customer_code,
                   customer_number,
                   name)
