# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper


class Address(object):

    """Implementation of the 'Address' model.

    TODO: type model description here.

    Attributes:
        address_type (AddressTypeEnum): Address type. 01 is for the receiver
            address, 02 is for the sender address.
        street (str): Street name; for Belgian addresses, it is strongly
            recommended to fill in the  street value
        house_nr (int): The house number of the delivery address
        house_nr_ext (str): House number extension
        zipcode (str): Zipcode of the address
        city (str): City of the address
        countrycode (CountrycodeEnum): ISO2 country code. Limited to NL and
            BE.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "address_type": 'AddressType',
        "house_nr": 'HouseNr',
        "zipcode": 'Zipcode',
        "countrycode": 'Countrycode',
        "street": 'Street',
        "house_nr_ext": 'HouseNrExt',
        "city": 'City'
    }

    _optionals = [
        'street',
        'house_nr_ext',
        'city',
    ]

    def __init__(self,
                 address_type=None,
                 house_nr=None,
                 zipcode=None,
                 countrycode=None,
                 street=APIHelper.SKIP,
                 house_nr_ext=APIHelper.SKIP,
                 city=APIHelper.SKIP):
        """Constructor for the Address class"""

        # Initialize members of the class
        self.address_type = address_type 
        if street is not APIHelper.SKIP:
            self.street = street 
        self.house_nr = house_nr 
        if house_nr_ext is not APIHelper.SKIP:
            self.house_nr_ext = house_nr_ext 
        self.zipcode = zipcode 
        if city is not APIHelper.SKIP:
            self.city = city 
        self.countrycode = countrycode 

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
        address_type = dictionary.get("AddressType") if dictionary.get("AddressType") else None
        house_nr = dictionary.get("HouseNr") if dictionary.get("HouseNr") else None
        zipcode = dictionary.get("Zipcode") if dictionary.get("Zipcode") else None
        countrycode = dictionary.get("Countrycode") if dictionary.get("Countrycode") else None
        street = dictionary.get("Street") if dictionary.get("Street") else APIHelper.SKIP
        house_nr_ext = dictionary.get("HouseNrExt") if dictionary.get("HouseNrExt") else APIHelper.SKIP
        city = dictionary.get("City") if dictionary.get("City") else APIHelper.SKIP
        # Return an object of this model
        return cls(address_type,
                   house_nr,
                   zipcode,
                   countrycode,
                   street,
                   house_nr_ext,
                   city)
