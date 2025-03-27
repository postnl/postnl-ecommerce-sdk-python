# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper
from postnlecommerce.models.no_timeframes_options import NoTimeframesOptions
from postnlecommerce.models.sustainability import Sustainability


class ReasonNoTimeframe(object):

    """Implementation of the 'ReasonNoTimeframe' model.

    Attributes:
        code (str): The reason code
        date (str): The date associated with the reason no timeframe was
            calculated
        description (str): The description associated with the reason no
            timeframe was calculated
        options (NoTimeframesOptions): The option for which no timeframe was
            calculated for a specific date
        sustainability (Sustainability): Sustainability score; see
            [Sustainability
            codes](https://developer.postnl.nl/docs/#/http/reference-data/refer
            ence-codes/sustainability-codes) for possible values.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "code": 'Code',
        "date": 'Date',
        "description": 'Description',
        "options": 'Options',
        "sustainability": 'Sustainability'
    }

    _optionals = [
        'code',
        'date',
        'description',
        'options',
        'sustainability',
    ]

    def __init__(self,
                 code=APIHelper.SKIP,
                 date=APIHelper.SKIP,
                 description=APIHelper.SKIP,
                 options=APIHelper.SKIP,
                 sustainability=APIHelper.SKIP):
        """Constructor for the ReasonNoTimeframe class"""

        # Initialize members of the class
        if code is not APIHelper.SKIP:
            self.code = code 
        if date is not APIHelper.SKIP:
            self.date = date 
        if description is not APIHelper.SKIP:
            self.description = description 
        if options is not APIHelper.SKIP:
            self.options = options 
        if sustainability is not APIHelper.SKIP:
            self.sustainability = sustainability 

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
        code = dictionary.get("Code") if dictionary.get("Code") else APIHelper.SKIP
        date = dictionary.get("Date") if dictionary.get("Date") else APIHelper.SKIP
        description = dictionary.get("Description") if dictionary.get("Description") else APIHelper.SKIP
        options = NoTimeframesOptions.from_dictionary(dictionary.get('Options')) if 'Options' in dictionary.keys() else APIHelper.SKIP
        sustainability = Sustainability.from_dictionary(dictionary.get('Sustainability')) if 'Sustainability' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(code,
                   date,
                   description,
                   options,
                   sustainability)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'code={(self.code if hasattr(self, "code") else None)!r}, '
                f'date={(self.date if hasattr(self, "date") else None)!r}, '
                f'description={(self.description if hasattr(self, "description") else None)!r}, '
                f'options={(self.options if hasattr(self, "options") else None)!r}, '
                f'sustainability={(self.sustainability if hasattr(self, "sustainability") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'code={(self.code if hasattr(self, "code") else None)!s}, '
                f'date={(self.date if hasattr(self, "date") else None)!s}, '
                f'description={(self.description if hasattr(self, "description") else None)!s}, '
                f'options={(self.options if hasattr(self, "options") else None)!s}, '
                f'sustainability={(self.sustainability if hasattr(self, "sustainability") else None)!s})')
