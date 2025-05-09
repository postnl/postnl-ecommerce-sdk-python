# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper


class LabellingCustomsContent(object):

    """Implementation of the 'labellingCustomsContent' model.

    Attributes:
        description (str): Description of goods
        quantity (int): Fill in the total of the item(s)
        weight (int): Net weight of goods in gram(gr)
        value (float): Commercial (customs) value of goods. Fill in the value
            of the item(s).
        hs_tariff_nr (str): Specify every item with the standard HS commodity
            code (HS-code), [more
            information](https://tarief.douane.nl/ite-tariff-public/#/home)
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
        """Constructor for the LabellingCustomsContent class"""

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

        if not isinstance(dictionary, dict) or dictionary is None:
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

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'description={self.description!r}, '
                f'quantity={self.quantity!r}, '
                f'weight={self.weight!r}, '
                f'value={self.value!r}, '
                f'hs_tariff_nr={(self.hs_tariff_nr if hasattr(self, "hs_tariff_nr") else None)!r}, '
                f'country_of_origin={(self.country_of_origin if hasattr(self, "country_of_origin") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'description={self.description!s}, '
                f'quantity={self.quantity!s}, '
                f'weight={self.weight!s}, '
                f'value={self.value!s}, '
                f'hs_tariff_nr={(self.hs_tariff_nr if hasattr(self, "hs_tariff_nr") else None)!s}, '
                f'country_of_origin={(self.country_of_origin if hasattr(self, "country_of_origin") else None)!s})')
