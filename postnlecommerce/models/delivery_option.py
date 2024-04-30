# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper
from postnlecommerce.models.timeframe import Timeframe


class DeliveryOption(object):

    """Implementation of the 'DeliveryOption' model.

    TODO: type model description here.

    Attributes:
        delivery_date (str): The possible delivery date
        timeframe (List[Timeframe]): Array of timeframes

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "delivery_date": 'DeliveryDate',
        "timeframe": 'Timeframe'
    }

    _optionals = [
        'delivery_date',
        'timeframe',
    ]

    def __init__(self,
                 delivery_date=APIHelper.SKIP,
                 timeframe=APIHelper.SKIP):
        """Constructor for the DeliveryOption class"""

        # Initialize members of the class
        if delivery_date is not APIHelper.SKIP:
            self.delivery_date = delivery_date 
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
        delivery_date = dictionary.get("DeliveryDate") if dictionary.get("DeliveryDate") else APIHelper.SKIP
        timeframe = None
        if dictionary.get('Timeframe') is not None:
            timeframe = [Timeframe.from_dictionary(x) for x in dictionary.get('Timeframe')]
        else:
            timeframe = APIHelper.SKIP
        # Return an object of this model
        return cls(delivery_date,
                   timeframe)
