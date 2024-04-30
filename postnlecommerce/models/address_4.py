# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper


class Address4(object):

    """Implementation of the 'Address4' model.

    TODO: type model description here.

    Attributes:
        first_name (str): The first name
        last_name (str): The last name
        company_name (str): The company name
        department_name (str): The department name
        country_code (str): The ISO2 country code
        zipcode (str): The zipcode
        region (str): The region name
        district (str): The district name
        city (str): The city name
        street (str): The street name
        house_number (str): The house number
        house_number_suffix (str): The house number suffix
        building (str): The building name
        floor (str): The floor of the building
        remark (str): An additional remark

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "first_name": 'FirstName',
        "last_name": 'LastName',
        "company_name": 'CompanyName',
        "department_name": 'DepartmentName',
        "country_code": 'CountryCode',
        "zipcode": 'Zipcode',
        "region": 'Region',
        "district": 'District',
        "city": 'City',
        "street": 'Street',
        "house_number": 'HouseNumber',
        "house_number_suffix": 'HouseNumberSuffix',
        "building": 'Building',
        "floor": 'Floor',
        "remark": 'Remark'
    }

    _optionals = [
        'first_name',
        'last_name',
        'company_name',
        'department_name',
        'country_code',
        'zipcode',
        'region',
        'district',
        'city',
        'street',
        'house_number',
        'house_number_suffix',
        'building',
        'floor',
        'remark',
    ]

    def __init__(self,
                 first_name=APIHelper.SKIP,
                 last_name=APIHelper.SKIP,
                 company_name=APIHelper.SKIP,
                 department_name=APIHelper.SKIP,
                 country_code=APIHelper.SKIP,
                 zipcode=APIHelper.SKIP,
                 region=APIHelper.SKIP,
                 district=APIHelper.SKIP,
                 city=APIHelper.SKIP,
                 street=APIHelper.SKIP,
                 house_number=APIHelper.SKIP,
                 house_number_suffix=APIHelper.SKIP,
                 building=APIHelper.SKIP,
                 floor=APIHelper.SKIP,
                 remark=APIHelper.SKIP):
        """Constructor for the Address4 class"""

        # Initialize members of the class
        if first_name is not APIHelper.SKIP:
            self.first_name = first_name 
        if last_name is not APIHelper.SKIP:
            self.last_name = last_name 
        if company_name is not APIHelper.SKIP:
            self.company_name = company_name 
        if department_name is not APIHelper.SKIP:
            self.department_name = department_name 
        if country_code is not APIHelper.SKIP:
            self.country_code = country_code 
        if zipcode is not APIHelper.SKIP:
            self.zipcode = zipcode 
        if region is not APIHelper.SKIP:
            self.region = region 
        if district is not APIHelper.SKIP:
            self.district = district 
        if city is not APIHelper.SKIP:
            self.city = city 
        if street is not APIHelper.SKIP:
            self.street = street 
        if house_number is not APIHelper.SKIP:
            self.house_number = house_number 
        if house_number_suffix is not APIHelper.SKIP:
            self.house_number_suffix = house_number_suffix 
        if building is not APIHelper.SKIP:
            self.building = building 
        if floor is not APIHelper.SKIP:
            self.floor = floor 
        if remark is not APIHelper.SKIP:
            self.remark = remark 

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
        first_name = dictionary.get("FirstName") if dictionary.get("FirstName") else APIHelper.SKIP
        last_name = dictionary.get("LastName") if dictionary.get("LastName") else APIHelper.SKIP
        company_name = dictionary.get("CompanyName") if dictionary.get("CompanyName") else APIHelper.SKIP
        department_name = dictionary.get("DepartmentName") if dictionary.get("DepartmentName") else APIHelper.SKIP
        country_code = dictionary.get("CountryCode") if dictionary.get("CountryCode") else APIHelper.SKIP
        zipcode = dictionary.get("Zipcode") if dictionary.get("Zipcode") else APIHelper.SKIP
        region = dictionary.get("Region") if dictionary.get("Region") else APIHelper.SKIP
        district = dictionary.get("District") if dictionary.get("District") else APIHelper.SKIP
        city = dictionary.get("City") if dictionary.get("City") else APIHelper.SKIP
        street = dictionary.get("Street") if dictionary.get("Street") else APIHelper.SKIP
        house_number = dictionary.get("HouseNumber") if dictionary.get("HouseNumber") else APIHelper.SKIP
        house_number_suffix = dictionary.get("HouseNumberSuffix") if dictionary.get("HouseNumberSuffix") else APIHelper.SKIP
        building = dictionary.get("Building") if dictionary.get("Building") else APIHelper.SKIP
        floor = dictionary.get("Floor") if dictionary.get("Floor") else APIHelper.SKIP
        remark = dictionary.get("Remark") if dictionary.get("Remark") else APIHelper.SKIP
        # Return an object of this model
        return cls(first_name,
                   last_name,
                   company_name,
                   department_name,
                   country_code,
                   zipcode,
                   region,
                   district,
                   city,
                   street,
                   house_number,
                   house_number_suffix,
                   building,
                   floor,
                   remark)
