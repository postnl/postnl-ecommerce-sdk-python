# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper
from postnlecommerce.models.signature import Signature
from postnlecommerce.models.warnings import Warnings


class ShippingstatusResponseSignature(object):

    """Implementation of the 'shippingstatusResponseSignature' model.

    TODO: type model description here.

    Attributes:
        signature (Signature): TODO: type description here.
        warnings (Warnings): TODO: type description here.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "signature": 'Signature',
        "warnings": 'Warnings'
    }

    _optionals = [
        'signature',
        'warnings',
    ]

    def __init__(self,
                 signature=APIHelper.SKIP,
                 warnings=APIHelper.SKIP):
        """Constructor for the ShippingstatusResponseSignature class"""

        # Initialize members of the class
        if signature is not APIHelper.SKIP:
            self.signature = signature 
        if warnings is not APIHelper.SKIP:
            self.warnings = warnings 

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
        signature = Signature.from_dictionary(dictionary.get('Signature')) if 'Signature' in dictionary.keys() else APIHelper.SKIP
        warnings = Warnings.from_dictionary(dictionary.get('Warnings')) if 'Warnings' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(signature,
                   warnings)
