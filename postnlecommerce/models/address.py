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
        address_type (str): Type of the address. This is a code. You can find
            the possible values at [Address
            types](https://developer.postnl.nl/docs/#/http/reference-data/refer
            ence-codes/address-types)
        area (str): Area of the address
        buildingname (str): Building name of the address
        city (str): City of the address
        company_name (str): This field has a dependency with the field Name.
            One of both fields must be filled mandatory; using both fields is
            also allowed. Mandatory when AddressType is 09.
        countrycode (str): The ISO2 country codes
        department (str): Send to specific department of a company
        doorcode (str): Door code of address. Mandatory for some international
            shipments.
        first_name (str): Remark: please add FirstName and Name (lastname) of
            the receiver to improve the parcel tracking experience of your
            customer.
        floor (str): Send to specific floor of a company
        house_nr (str): Mandatory for shipments to Benelux. Max. length is 5
            characters (only for Benelux addresses). For Benelux
            addresses,this field should always be numeric.
        house_nr_ext (str): House number extension
        name (str): Last name of person. This field has a dependency with the
            field CompanyName. One of both fields must be filled mandatory;
            using both fields is also allowed. Remark: please add FirstName
            and Name (lastname) of the receiver to improve the parcel tracking
            experience of your customer.
        region (str): Region of the address. Mandatory for Non EU destinations
            where a region is applicable.
        street (str): This field has a dependency with the field
            StreetHouseNrExt. One of both fields must be filled mandatory.
            Using both fields simultaneously is discouraged.
        street_house_nr_ext (str): Combination of Street, HouseNr and
            HouseNrExt. Please see
            [Guidelines](https://developer.postnl.nl/docs/#/http/api-endpoints/
            send-track/confirming/guidelines) for the explanation.
        zipcode (str): Zipcode of the address. Mandatory for shipments to
            Benelux. Max length (NL) 6 characters,(BE;LU) 4 numeric
            characters

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "address_type": 'AddressType',
        "countrycode": 'Countrycode',
        "area": 'Area',
        "buildingname": 'Buildingname',
        "city": 'City',
        "company_name": 'CompanyName',
        "department": 'Department',
        "doorcode": 'Doorcode',
        "first_name": 'FirstName',
        "floor": 'Floor',
        "house_nr": 'HouseNr',
        "house_nr_ext": 'HouseNrExt',
        "name": 'Name',
        "region": 'Region',
        "street": 'Street',
        "street_house_nr_ext": 'StreetHouseNrExt',
        "zipcode": 'Zipcode'
    }

    _optionals = [
        'area',
        'buildingname',
        'city',
        'company_name',
        'department',
        'doorcode',
        'first_name',
        'floor',
        'house_nr',
        'house_nr_ext',
        'name',
        'region',
        'street',
        'street_house_nr_ext',
        'zipcode',
    ]

    def __init__(self,
                 address_type='01',
                 countrycode=None,
                 area=APIHelper.SKIP,
                 buildingname=APIHelper.SKIP,
                 city=APIHelper.SKIP,
                 company_name=APIHelper.SKIP,
                 department=APIHelper.SKIP,
                 doorcode=APIHelper.SKIP,
                 first_name=APIHelper.SKIP,
                 floor=APIHelper.SKIP,
                 house_nr=APIHelper.SKIP,
                 house_nr_ext=APIHelper.SKIP,
                 name=APIHelper.SKIP,
                 region=APIHelper.SKIP,
                 street=APIHelper.SKIP,
                 street_house_nr_ext=APIHelper.SKIP,
                 zipcode=APIHelper.SKIP):
        """Constructor for the Address class"""

        # Initialize members of the class
        self.address_type = address_type 
        if area is not APIHelper.SKIP:
            self.area = area 
        if buildingname is not APIHelper.SKIP:
            self.buildingname = buildingname 
        if city is not APIHelper.SKIP:
            self.city = city 
        if company_name is not APIHelper.SKIP:
            self.company_name = company_name 
        self.countrycode = countrycode 
        if department is not APIHelper.SKIP:
            self.department = department 
        if doorcode is not APIHelper.SKIP:
            self.doorcode = doorcode 
        if first_name is not APIHelper.SKIP:
            self.first_name = first_name 
        if floor is not APIHelper.SKIP:
            self.floor = floor 
        if house_nr is not APIHelper.SKIP:
            self.house_nr = house_nr 
        if house_nr_ext is not APIHelper.SKIP:
            self.house_nr_ext = house_nr_ext 
        if name is not APIHelper.SKIP:
            self.name = name 
        if region is not APIHelper.SKIP:
            self.region = region 
        if street is not APIHelper.SKIP:
            self.street = street 
        if street_house_nr_ext is not APIHelper.SKIP:
            self.street_house_nr_ext = street_house_nr_ext 
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
        address_type = dictionary.get("AddressType") if dictionary.get("AddressType") else '01'
        countrycode = dictionary.get("Countrycode") if dictionary.get("Countrycode") else None
        area = dictionary.get("Area") if dictionary.get("Area") else APIHelper.SKIP
        buildingname = dictionary.get("Buildingname") if dictionary.get("Buildingname") else APIHelper.SKIP
        city = dictionary.get("City") if dictionary.get("City") else APIHelper.SKIP
        company_name = dictionary.get("CompanyName") if dictionary.get("CompanyName") else APIHelper.SKIP
        department = dictionary.get("Department") if dictionary.get("Department") else APIHelper.SKIP
        doorcode = dictionary.get("Doorcode") if dictionary.get("Doorcode") else APIHelper.SKIP
        first_name = dictionary.get("FirstName") if dictionary.get("FirstName") else APIHelper.SKIP
        floor = dictionary.get("Floor") if dictionary.get("Floor") else APIHelper.SKIP
        house_nr = dictionary.get("HouseNr") if dictionary.get("HouseNr") else APIHelper.SKIP
        house_nr_ext = dictionary.get("HouseNrExt") if dictionary.get("HouseNrExt") else APIHelper.SKIP
        name = dictionary.get("Name") if dictionary.get("Name") else APIHelper.SKIP
        region = dictionary.get("Region") if dictionary.get("Region") else APIHelper.SKIP
        street = dictionary.get("Street") if dictionary.get("Street") else APIHelper.SKIP
        street_house_nr_ext = dictionary.get("StreetHouseNrExt") if dictionary.get("StreetHouseNrExt") else APIHelper.SKIP
        zipcode = dictionary.get("Zipcode") if dictionary.get("Zipcode") else APIHelper.SKIP
        # Return an object of this model
        return cls(address_type,
                   countrycode,
                   area,
                   buildingname,
                   city,
                   company_name,
                   department,
                   doorcode,
                   first_name,
                   floor,
                   house_nr,
                   house_nr_ext,
                   name,
                   region,
                   street,
                   street_house_nr_ext,
                   zipcode)
