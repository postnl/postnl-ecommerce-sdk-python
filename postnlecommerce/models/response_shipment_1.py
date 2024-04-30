# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper
from postnlecommerce.models.label_1 import Label1
from postnlecommerce.models.warning_1 import Warning1


class ResponseShipment1(object):

    """Implementation of the 'ResponseShipment1' model.

    TODO: type model description here.

    Attributes:
        product_code_delivery (str): The product code of the shipment
        labels (List[Label1]): All labels belonging to the selected product
        barcode (str): The barcode used on the label
        warnings (List[Warning1]): Possible warnings. See the [Error
            Codes](#tag/Error-codes) for possible values

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "product_code_delivery": 'ProductCodeDelivery',
        "labels": 'Labels',
        "barcode": 'Barcode',
        "warnings": 'Warnings'
    }

    _optionals = [
        'product_code_delivery',
        'labels',
        'barcode',
        'warnings',
    ]

    def __init__(self,
                 product_code_delivery=APIHelper.SKIP,
                 labels=APIHelper.SKIP,
                 barcode=APIHelper.SKIP,
                 warnings=APIHelper.SKIP):
        """Constructor for the ResponseShipment1 class"""

        # Initialize members of the class
        if product_code_delivery is not APIHelper.SKIP:
            self.product_code_delivery = product_code_delivery 
        if labels is not APIHelper.SKIP:
            self.labels = labels 
        if barcode is not APIHelper.SKIP:
            self.barcode = barcode 
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
        product_code_delivery = dictionary.get("ProductCodeDelivery") if dictionary.get("ProductCodeDelivery") else APIHelper.SKIP
        labels = None
        if dictionary.get('Labels') is not None:
            labels = [Label1.from_dictionary(x) for x in dictionary.get('Labels')]
        else:
            labels = APIHelper.SKIP
        barcode = dictionary.get("Barcode") if dictionary.get("Barcode") else APIHelper.SKIP
        warnings = None
        if dictionary.get('Warnings') is not None:
            warnings = [Warning1.from_dictionary(x) for x in dictionary.get('Warnings')]
        else:
            warnings = APIHelper.SKIP
        # Return an object of this model
        return cls(product_code_delivery,
                   labels,
                   barcode,
                   warnings)
