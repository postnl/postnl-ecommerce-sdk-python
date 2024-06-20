# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper
from postnlecommerce.models.shippingstatus_warning import ShippingstatusWarning


class Warnings(object):

    """Implementation of the 'Warnings' model.

    TODO: type model description here.

    Attributes:
        warning (ShippingstatusWarning): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "warning": 'Warning'
    }

    _optionals = [
        'warning',
    ]

    def __init__(self,
                 warning=APIHelper.SKIP):
        """Constructor for the Warnings class"""

        # Initialize members of the class
        if warning is not APIHelper.SKIP:
            self.warning = warning 

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
        warning = ShippingstatusWarning.from_dictionary(dictionary.get('Warning')) if 'Warning' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(warning)
