# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper
from postnlecommerce.models.updated_shipment_status import UpdatedShipmentStatus


class ShippingstatusResponseUpdatedShipment(object):

    """Implementation of the 'shippingstatusResponseUpdatedShipment' model.

    TODO: type model description here.

    Attributes:
        barcode (str): The barcode belonging to the status update
        creation_date (str): The date of the update
        customer_number (str): The customer number
        customer_code (str): The customer code
        status (UpdatedShipmentStatus): The status update. See [Status
            codes](https://developer.postnl.nl/docs/#/http/reference-data/error
            -codes) for possible values.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "barcode": 'Barcode',
        "creation_date": 'CreationDate',
        "customer_number": 'CustomerNumber',
        "customer_code": 'CustomerCode',
        "status": 'Status'
    }

    _optionals = [
        'barcode',
        'creation_date',
        'customer_number',
        'customer_code',
        'status',
    ]

    def __init__(self,
                 barcode=APIHelper.SKIP,
                 creation_date=APIHelper.SKIP,
                 customer_number=APIHelper.SKIP,
                 customer_code=APIHelper.SKIP,
                 status=APIHelper.SKIP):
        """Constructor for the ShippingstatusResponseUpdatedShipment class"""

        # Initialize members of the class
        if barcode is not APIHelper.SKIP:
            self.barcode = barcode 
        if creation_date is not APIHelper.SKIP:
            self.creation_date = creation_date 
        if customer_number is not APIHelper.SKIP:
            self.customer_number = customer_number 
        if customer_code is not APIHelper.SKIP:
            self.customer_code = customer_code 
        if status is not APIHelper.SKIP:
            self.status = status 

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
        creation_date = dictionary.get("CreationDate") if dictionary.get("CreationDate") else APIHelper.SKIP
        customer_number = dictionary.get("CustomerNumber") if dictionary.get("CustomerNumber") else APIHelper.SKIP
        customer_code = dictionary.get("CustomerCode") if dictionary.get("CustomerCode") else APIHelper.SKIP
        status = UpdatedShipmentStatus.from_dictionary(dictionary.get('Status')) if 'Status' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(barcode,
                   creation_date,
                   customer_number,
                   customer_code,
                   status)
