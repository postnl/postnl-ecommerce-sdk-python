# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper
from postnlecommerce.models.reason_no_timeframe import ReasonNoTimeframe


class ReasonNoTimeframes(object):

    """Implementation of the 'ReasonNoTimeframes' model.

    TODO: type model description here.

    Attributes:
        reason_no_timeframe (List[ReasonNoTimeframe]): The reason why no
            timeframe was returned

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "reason_no_timeframe": 'ReasonNoTimeframe'
    }

    _optionals = [
        'reason_no_timeframe',
    ]

    def __init__(self,
                 reason_no_timeframe=APIHelper.SKIP):
        """Constructor for the ReasonNoTimeframes class"""

        # Initialize members of the class
        if reason_no_timeframe is not APIHelper.SKIP:
            self.reason_no_timeframe = reason_no_timeframe 

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
        reason_no_timeframe = None
        if dictionary.get('ReasonNoTimeframe') is not None:
            reason_no_timeframe = [ReasonNoTimeframe.from_dictionary(x) for x in dictionary.get('ReasonNoTimeframe')]
        else:
            reason_no_timeframe = APIHelper.SKIP
        # Return an object of this model
        return cls(reason_no_timeframe)
