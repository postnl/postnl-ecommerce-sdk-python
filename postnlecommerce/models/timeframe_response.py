# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper
from postnlecommerce.models.reason_no_timeframes import ReasonNoTimeframes
from postnlecommerce.models.timeframes import Timeframes


class TimeframeResponse(object):

    """Implementation of the 'timeframeResponse' model.

    TODO: type model description here.

    Attributes:
        timeframes (Timeframes): TODO: type description here.
        reason_no_timeframes (ReasonNoTimeframes): TODO: type description
            here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "timeframes": 'Timeframes',
        "reason_no_timeframes": 'ReasonNoTimeframes'
    }

    _optionals = [
        'timeframes',
        'reason_no_timeframes',
    ]

    def __init__(self,
                 timeframes=APIHelper.SKIP,
                 reason_no_timeframes=APIHelper.SKIP):
        """Constructor for the TimeframeResponse class"""

        # Initialize members of the class
        if timeframes is not APIHelper.SKIP:
            self.timeframes = timeframes 
        if reason_no_timeframes is not APIHelper.SKIP:
            self.reason_no_timeframes = reason_no_timeframes 

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
        timeframes = Timeframes.from_dictionary(dictionary.get('Timeframes')) if 'Timeframes' in dictionary.keys() else APIHelper.SKIP
        reason_no_timeframes = ReasonNoTimeframes.from_dictionary(dictionary.get('ReasonNoTimeframes')) if 'ReasonNoTimeframes' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(timeframes,
                   reason_no_timeframes)
