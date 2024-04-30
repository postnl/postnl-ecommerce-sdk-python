# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper
from postnlecommerce.models.timeframe_timeframe import TimeframeTimeframe


class Timeframes1(object):

    """Implementation of the 'Timeframes1' model.

    TODO: type model description here.

    Attributes:
        timeframe_timeframe (List[TimeframeTimeframe]): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "timeframe_timeframe": 'TimeframeTimeframe'
    }

    _optionals = [
        'timeframe_timeframe',
    ]

    def __init__(self,
                 timeframe_timeframe=APIHelper.SKIP):
        """Constructor for the Timeframes1 class"""

        # Initialize members of the class
        if timeframe_timeframe is not APIHelper.SKIP:
            self.timeframe_timeframe = timeframe_timeframe 

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
        timeframe_timeframe = None
        if dictionary.get('TimeframeTimeframe') is not None:
            timeframe_timeframe = [TimeframeTimeframe.from_dictionary(x) for x in dictionary.get('TimeframeTimeframe')]
        else:
            timeframe_timeframe = APIHelper.SKIP
        # Return an object of this model
        return cls(timeframe_timeframe)
