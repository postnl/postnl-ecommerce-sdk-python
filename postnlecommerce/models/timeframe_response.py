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

    Attributes:
        timeframes (Timeframes): The model property of type Timeframes.
        reason_no_timeframes (ReasonNoTimeframes): The model property of type
            ReasonNoTimeframes.

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

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        timeframes = Timeframes.from_dictionary(dictionary.get('Timeframes')) if 'Timeframes' in dictionary.keys() else APIHelper.SKIP
        reason_no_timeframes = ReasonNoTimeframes.from_dictionary(dictionary.get('ReasonNoTimeframes')) if 'ReasonNoTimeframes' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(timeframes,
                   reason_no_timeframes)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'timeframes={(self.timeframes if hasattr(self, "timeframes") else None)!r}, '
                f'reason_no_timeframes={(self.reason_no_timeframes if hasattr(self, "reason_no_timeframes") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'timeframes={(self.timeframes if hasattr(self, "timeframes") else None)!s}, '
                f'reason_no_timeframes={(self.reason_no_timeframes if hasattr(self, "reason_no_timeframes") else None)!s})')
