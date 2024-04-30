# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper


class Content(object):

    """Implementation of the 'Content' model.

    TODO: type model description here.

    Attributes:
        description (str): Description of goods
        quantity (int): Fill in the total of the item(s)
        weight (int): Net weight of goods in gram(gr)
        value (float): Commercial (customs) value of goods. Fill in the value
            of the item(s).
        hs_tariff_nr (str): Specify every item with the standard HS commodity
            code (6-8-10 digits HS-code), [more
            information](https://tarief.douane.nl/arctictariff-public-web/#!/ho
            me). Note: punctuation marks and symbols are not allowed.
        country_of_origin (str): Fill in the code of the country where the
            item was produced (ISO-code), [more
            information](https://www.iso.org/home.html)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "description": 'Description',
        "quantity": 'Quantity',
        "weight": 'Weight',
        "value": 'Value',
        "hs_tariff_nr": 'HSTariffNr',
        "country_of_origin": 'CountryOfOrigin'
    }

    _optionals = [
        'hs_tariff_nr',
        'country_of_origin',
    ]

    def __init__(self,
                 description=None,
                 quantity=None,
                 weight=None,
                 value=None,
                 hs_tariff_nr=APIHelper.SKIP,
                 country_of_origin=APIHelper.SKIP):
        """Constructor for the Content class"""

        # Initialize members of the class
        self.description = description 
        self.quantity = quantity 
        self.weight = weight 
        self.value = value 
        if hs_tariff_nr is not APIHelper.SKIP:
            self.hs_tariff_nr = hs_tariff_nr 
        if country_of_origin is not APIHelper.SKIP:
            self.country_of_origin = country_of_origin 

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
        description = dictionary.get("Description") if dictionary.get("Description") else None
        quantity = dictionary.get("Quantity") if dictionary.get("Quantity") else None
        weight = dictionary.get("Weight") if dictionary.get("Weight") else None
        value = dictionary.get("Value") if dictionary.get("Value") else None
        hs_tariff_nr = dictionary.get("HSTariffNr") if dictionary.get("HSTariffNr") else APIHelper.SKIP
        country_of_origin = dictionary.get("CountryOfOrigin") if dictionary.get("CountryOfOrigin") else APIHelper.SKIP
        # Return an object of this model
        return cls(description,
                   quantity,
                   weight,
                   value,
                   hs_tariff_nr,
                   country_of_origin)
