# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper
from postnlecommerce.models.customer_address import CustomerAddress


class Customer(object):

    """Implementation of the 'Customer' model.

    TODO: type model description here.

    Attributes:
        address (CustomerAddress): TODO: type description here.
        collection_location (str): Code of delivery location at PostNL
            Pakketten
        contact_person (str): Name of customer contact person
        customer_code (str): Customer code as known at PostNL Pakketten
        customer_number (str): Name of customer contact person
        email (str): E-mail address of the customer. Mandatory for Non EU
            destinations.
        name (str): Customer name

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "customer_code": 'CustomerCode',
        "customer_number": 'CustomerNumber',
        "address": 'Address',
        "collection_location": 'CollectionLocation',
        "contact_person": 'ContactPerson',
        "email": 'Email',
        "name": 'Name'
    }

    _optionals = [
        'address',
        'collection_location',
        'contact_person',
        'email',
        'name',
    ]

    def __init__(self,
                 customer_code=None,
                 customer_number=None,
                 address=APIHelper.SKIP,
                 collection_location=APIHelper.SKIP,
                 contact_person=APIHelper.SKIP,
                 email=APIHelper.SKIP,
                 name=APIHelper.SKIP):
        """Constructor for the Customer class"""

        # Initialize members of the class
        if address is not APIHelper.SKIP:
            self.address = address 
        if collection_location is not APIHelper.SKIP:
            self.collection_location = collection_location 
        if contact_person is not APIHelper.SKIP:
            self.contact_person = contact_person 
        self.customer_code = customer_code 
        self.customer_number = customer_number 
        if email is not APIHelper.SKIP:
            self.email = email 
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
        customer_code = dictionary.get("CustomerCode") if dictionary.get("CustomerCode") else None
        customer_number = dictionary.get("CustomerNumber") if dictionary.get("CustomerNumber") else None
        address = CustomerAddress.from_dictionary(dictionary.get('Address')) if 'Address' in dictionary.keys() else APIHelper.SKIP
        collection_location = dictionary.get("CollectionLocation") if dictionary.get("CollectionLocation") else APIHelper.SKIP
        contact_person = dictionary.get("ContactPerson") if dictionary.get("ContactPerson") else APIHelper.SKIP
        email = dictionary.get("Email") if dictionary.get("Email") else APIHelper.SKIP
        name = dictionary.get("Name") if dictionary.get("Name") else APIHelper.SKIP
        # Return an object of this model
        return cls(customer_code,
                   customer_number,
                   address,
                   collection_location,
                   contact_person,
                   email,
                   name)
