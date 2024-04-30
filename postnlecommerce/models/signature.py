# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper


class Signature(object):

    """Implementation of the 'Signature' model.

    TODO: type model description here.

    Attributes:
        barcode (str): The barcode of the shipment for which the signature is
            returned
        signature_date (str): The date of the signature
        signature_image (str): The signature content; base64 encoded GIF
            format.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "barcode": 'Barcode',
        "signature_date": 'SignatureDate',
        "signature_image": 'SignatureImage'
    }

    _optionals = [
        'barcode',
        'signature_date',
        'signature_image',
    ]

    def __init__(self,
                 barcode=APIHelper.SKIP,
                 signature_date=APIHelper.SKIP,
                 signature_image=APIHelper.SKIP):
        """Constructor for the Signature class"""

        # Initialize members of the class
        if barcode is not APIHelper.SKIP:
            self.barcode = barcode 
        if signature_date is not APIHelper.SKIP:
            self.signature_date = signature_date 
        if signature_image is not APIHelper.SKIP:
            self.signature_image = signature_image 

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
        barcode = dictionary.get("Barcode") if dictionary.get("Barcode") else APIHelper.SKIP
        signature_date = dictionary.get("SignatureDate") if dictionary.get("SignatureDate") else APIHelper.SKIP
        signature_image = dictionary.get("SignatureImage") if dictionary.get("SignatureImage") else APIHelper.SKIP
        # Return an object of this model
        return cls(barcode,
                   signature_date,
                   signature_image)
