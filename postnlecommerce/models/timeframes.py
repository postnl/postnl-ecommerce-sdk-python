# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper
from postnlecommerce.models.timeframe import Timeframe


class Timeframes(object):

    """Implementation of the 'Timeframes' model.

    TODO: type model description here.

    Attributes:
        timeframe (List[Timeframe]): A calculated delivery timeframe

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "timeframe": 'Timeframe'
    }

    _optionals = [
        'timeframe',
    ]

    def __init__(self,
                 timeframe=APIHelper.SKIP):
        """Constructor for the Timeframes class"""

        # Initialize members of the class
        if timeframe is not APIHelper.SKIP:
            self.timeframe = timeframe 

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
        timeframe = None
        if dictionary.get('Timeframe') is not None:
            timeframe = [Timeframe.from_dictionary(x) for x in dictionary.get('Timeframe')]
        else:
            timeframe = APIHelper.SKIP
        # Return an object of this model
        return cls(timeframe)
