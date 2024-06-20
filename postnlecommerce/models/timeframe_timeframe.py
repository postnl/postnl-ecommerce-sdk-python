# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper
from postnlecommerce.models.options import Options
from postnlecommerce.models.sustainability import Sustainability


class TimeframeTimeframe(object):

    """Implementation of the 'TimeframeTimeframe' model.

    TODO: type model description here.

    Attributes:
        mfrom (str): The start time of the expected delivery window
        options (Options): The delivery option for which the timeframe is
            calculated. See [Delivery
            Options](https://developer.postnl.nl/docs/#/http/reference-data/ref
            erence-codes/delivery-options) for possible values.
        to (str): The end time of the expected delivery window
        sustainability (Sustainability): Sustainability score; see
            [Sustainability
            codes](https://developer.postnl.nl/docs/#/http/reference-data/refer
            ence-codes) for possible values.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "mfrom": 'From',
        "options": 'Options',
        "to": 'To',
        "sustainability": 'Sustainability'
    }

    _optionals = [
        'mfrom',
        'options',
        'to',
        'sustainability',
    ]

    def __init__(self,
                 mfrom=APIHelper.SKIP,
                 options=APIHelper.SKIP,
                 to=APIHelper.SKIP,
                 sustainability=APIHelper.SKIP):
        """Constructor for the TimeframeTimeframe class"""

        # Initialize members of the class
        if mfrom is not APIHelper.SKIP:
            self.mfrom = mfrom 
        if options is not APIHelper.SKIP:
            self.options = options 
        if to is not APIHelper.SKIP:
            self.to = to 
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

        if dictionary is None:
            return None

        # Extract variables from the dictionary
        mfrom = dictionary.get("From") if dictionary.get("From") else APIHelper.SKIP
        options = Options.from_dictionary(dictionary.get('Options')) if 'Options' in dictionary.keys() else APIHelper.SKIP
        to = dictionary.get("To") if dictionary.get("To") else APIHelper.SKIP
        sustainability = Sustainability.from_dictionary(dictionary.get('Sustainability')) if 'Sustainability' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(mfrom,
                   options,
                   to,
                   sustainability)
