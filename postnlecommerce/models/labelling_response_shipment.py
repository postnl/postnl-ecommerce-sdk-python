# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper
from postnlecommerce.models.labelling_label import LabellingLabel
from postnlecommerce.models.warning import Warning


class LabellingResponseShipment(object):

    """Implementation of the 'labellingResponseShipment' model.

    TODO: type model description here.

    Attributes:
        product_code_delivery (str): The product code of the shipment
        labels (List[LabellingLabel]): All labels belonging to the selected
            product
        barcode (str): The barcode used on the label
        errors (List[object]): TODO: type description here.
        warnings (List[Warning]): Possible warnings. See the [Error
            Codes](https://developer.postnl.nl/docs/#/http/reference-data/error
            -codes) for possible values

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "product_code_delivery": 'ProductCodeDelivery',
        "labels": 'Labels',
        "barcode": 'Barcode',
        "errors": 'Errors',
        "warnings": 'Warnings'
    }

    _optionals = [
        'product_code_delivery',
        'labels',
        'barcode',
        'errors',
        'warnings',
    ]

    def __init__(self,
                 product_code_delivery=APIHelper.SKIP,
                 labels=APIHelper.SKIP,
                 barcode=APIHelper.SKIP,
                 errors=APIHelper.SKIP,
                 warnings=APIHelper.SKIP):
        """Constructor for the LabellingResponseShipment class"""

        # Initialize members of the class
        if product_code_delivery is not APIHelper.SKIP:
            self.product_code_delivery = product_code_delivery 
        if labels is not APIHelper.SKIP:
            self.labels = labels 
        if barcode is not APIHelper.SKIP:
            self.barcode = barcode 
        if errors is not APIHelper.SKIP:
            self.errors = errors 
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
            labels = [LabellingLabel.from_dictionary(x) for x in dictionary.get('Labels')]
        else:
            labels = APIHelper.SKIP
        barcode = dictionary.get("Barcode") if dictionary.get("Barcode") else APIHelper.SKIP
        errors = dictionary.get("Errors") if dictionary.get("Errors") else APIHelper.SKIP
        warnings = None
        if dictionary.get('Warnings') is not None:
            warnings = [Warning.from_dictionary(x) for x in dictionary.get('Warnings')]
        else:
            warnings = APIHelper.SKIP
        # Return an object of this model
        return cls(product_code_delivery,
                   labels,
                   barcode,
                   errors,
                   warnings)
