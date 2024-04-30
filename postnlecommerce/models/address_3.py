# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper


class Address3(object):

    """Implementation of the 'Address3' model.

    TODO: type model description here.

    Attributes:
        city (str): The city of the pickup location address
        countrycode (str): The country of the pickup location address
        house_nr (int): The house number of the pickup location address
        house_nr_ext (str): The house number extension of the pickup location
            address
        remark (str): Additional information about the pickup location
        street (str): The street of the pickup location address
        zipcode (str): The zipcode of the pickup location address

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "city": 'City',
        "countrycode": 'Countrycode',
        "house_nr": 'HouseNr',
        "house_nr_ext": 'HouseNrExt',
        "remark": 'Remark',
        "street": 'Street',
        "zipcode": 'Zipcode'
    }

    _optionals = [
        'city',
        'countrycode',
        'house_nr',
        'house_nr_ext',
        'remark',
        'street',
        'zipcode',
    ]

    def __init__(self,
                 city=APIHelper.SKIP,
                 countrycode=APIHelper.SKIP,
                 house_nr=APIHelper.SKIP,
                 house_nr_ext=APIHelper.SKIP,
                 remark=APIHelper.SKIP,
                 street=APIHelper.SKIP,
                 zipcode=APIHelper.SKIP):
        """Constructor for the Address3 class"""

        # Initialize members of the class
        if city is not APIHelper.SKIP:
            self.city = city 
        if countrycode is not APIHelper.SKIP:
            self.countrycode = countrycode 
        if house_nr is not APIHelper.SKIP:
            self.house_nr = house_nr 
        if house_nr_ext is not APIHelper.SKIP:
            self.house_nr_ext = house_nr_ext 
        if remark is not APIHelper.SKIP:
            self.remark = remark 
        if street is not APIHelper.SKIP:
            self.street = street 
        if zipcode is not APIHelper.SKIP:
            self.zipcode = zipcode 

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
        city = dictionary.get("City") if dictionary.get("City") else APIHelper.SKIP
        countrycode = dictionary.get("Countrycode") if dictionary.get("Countrycode") else APIHelper.SKIP
        house_nr = dictionary.get("HouseNr") if dictionary.get("HouseNr") else APIHelper.SKIP
        house_nr_ext = dictionary.get("HouseNrExt") if dictionary.get("HouseNrExt") else APIHelper.SKIP
        remark = dictionary.get("Remark") if dictionary.get("Remark") else APIHelper.SKIP
        street = dictionary.get("Street") if dictionary.get("Street") else APIHelper.SKIP
        zipcode = dictionary.get("Zipcode") if dictionary.get("Zipcode") else APIHelper.SKIP
        # Return an object of this model
        return cls(city,
                   countrycode,
                   house_nr,
                   house_nr_ext,
                   remark,
                   street,
                   zipcode)
