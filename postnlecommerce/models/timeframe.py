# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper
from postnlecommerce.models.timeframes_response_object import TimeframesResponseObject


class Timeframe(object):

    """Implementation of the 'Timeframe' model.

    Attributes:
        date (str): The expected date of delivery
        timeframes (TimeframesResponseObject): The model property of type
            TimeframesResponseObject.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "date": 'Date',
        "timeframes": 'Timeframes'
    }

    _optionals = [
        'date',
        'timeframes',
    ]

    def __init__(self,
                 date=APIHelper.SKIP,
                 timeframes=APIHelper.SKIP):
        """Constructor for the Timeframe class"""

        # Initialize members of the class
        if date is not APIHelper.SKIP:
            self.date = date 
        if timeframes is not APIHelper.SKIP:
            self.timeframes = timeframes 

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
        date = dictionary.get("Date") if dictionary.get("Date") else APIHelper.SKIP
        timeframes = TimeframesResponseObject.from_dictionary(dictionary.get('Timeframes')) if 'Timeframes' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(date,
                   timeframes)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'date={(self.date if hasattr(self, "date") else None)!r}, '
                f'timeframes={(self.timeframes if hasattr(self, "timeframes") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'date={(self.date if hasattr(self, "date") else None)!s}, '
                f'timeframes={(self.timeframes if hasattr(self, "timeframes") else None)!s})')
