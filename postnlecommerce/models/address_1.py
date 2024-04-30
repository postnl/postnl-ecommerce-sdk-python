# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper


class Address1(object):

    """Implementation of the 'Address1' model.

    The pickup location address

    Attributes:
        street (str): The pickup location street
        zipcode (str): The pickup location zipcode
        house_nr (int): The pickup location housenumber
        house_nr_ext (str): The pickup location housenumber extension
        countrycode (str): The pickup location country
        company_name (str): The pickup location company name

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "street": 'Street',
        "zipcode": 'Zipcode',
        "house_nr": 'HouseNr',
        "house_nr_ext": 'HouseNrExt',
        "countrycode": 'Countrycode',
        "company_name": 'CompanyName'
    }

    _optionals = [
        'street',
        'zipcode',
        'house_nr',
        'house_nr_ext',
        'countrycode',
        'company_name',
    ]

    def __init__(self,
                 street=APIHelper.SKIP,
                 zipcode=APIHelper.SKIP,
                 house_nr=APIHelper.SKIP,
                 house_nr_ext=APIHelper.SKIP,
                 countrycode=APIHelper.SKIP,
                 company_name=APIHelper.SKIP):
        """Constructor for the Address1 class"""

        # Initialize members of the class
        if street is not APIHelper.SKIP:
            self.street = street 
        if zipcode is not APIHelper.SKIP:
            self.zipcode = zipcode 
        if house_nr is not APIHelper.SKIP:
            self.house_nr = house_nr 
        if house_nr_ext is not APIHelper.SKIP:
            self.house_nr_ext = house_nr_ext 
        if countrycode is not APIHelper.SKIP:
            self.countrycode = countrycode 
        if company_name is not APIHelper.SKIP:
            self.company_name = company_name 

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
        street = dictionary.get("Street") if dictionary.get("Street") else APIHelper.SKIP
        zipcode = dictionary.get("Zipcode") if dictionary.get("Zipcode") else APIHelper.SKIP
        house_nr = dictionary.get("HouseNr") if dictionary.get("HouseNr") else APIHelper.SKIP
        house_nr_ext = dictionary.get("HouseNrExt") if dictionary.get("HouseNrExt") else APIHelper.SKIP
        countrycode = dictionary.get("Countrycode") if dictionary.get("Countrycode") else APIHelper.SKIP
        company_name = dictionary.get("CompanyName") if dictionary.get("CompanyName") else APIHelper.SKIP
        # Return an object of this model
        return cls(street,
                   zipcode,
                   house_nr,
                   house_nr_ext,
                   countrycode,
                   company_name)
