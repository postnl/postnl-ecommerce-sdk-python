# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper
from postnlecommerce.models.address_4 import Address4
from postnlecommerce.models.customer_2 import Customer2
from postnlecommerce.models.dimension_1 import Dimension1
from postnlecommerce.models.product_options import ProductOptions
from postnlecommerce.models.status import Status


class Shipment11(object):

    """Implementation of the 'Shipment11' model.

    TODO: type model description here.

    Attributes:
        main_barcode (str): The main barcode of the shipment
        barcode (str): The barcode of the shipment
        shipment_amount (str): The amount of parcels in the multi-collo
            shipment
        shipment_counter (str): The sequence of this parcel in the multi-collo
            shipment
        customer (Customer2): TODO: type description here.
        product_code (str): The product code of the shipment
        product_description (str): The description of the product code
        reference (str): The customer reference belonging to the shipment
        delivery_date (str): The expected delivery date of the shipment
        dimension (Dimension1): TODO: type description here.
        address (List[Address4]): A list of addresses belonging to the
            shipment
        product_options (ProductOptions): A list of product options.
        status (Status): The current status of the shipment (see the [Status
            codes](#tag/TandT-status-codes/Status-codes) for possible values.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "main_barcode": 'MainBarcode',
        "barcode": 'Barcode',
        "shipment_amount": 'ShipmentAmount',
        "shipment_counter": 'ShipmentCounter',
        "customer": 'Customer',
        "product_code": 'ProductCode',
        "product_description": 'ProductDescription',
        "reference": 'Reference',
        "delivery_date": 'DeliveryDate',
        "dimension": 'Dimension',
        "address": 'Address',
        "product_options": 'ProductOptions',
        "status": 'Status'
    }

    _optionals = [
        'main_barcode',
        'barcode',
        'shipment_amount',
        'shipment_counter',
        'customer',
        'product_code',
        'product_description',
        'reference',
        'delivery_date',
        'dimension',
        'address',
        'product_options',
        'status',
    ]

    def __init__(self,
                 main_barcode=APIHelper.SKIP,
                 barcode=APIHelper.SKIP,
                 shipment_amount=APIHelper.SKIP,
                 shipment_counter=APIHelper.SKIP,
                 customer=APIHelper.SKIP,
                 product_code=APIHelper.SKIP,
                 product_description=APIHelper.SKIP,
                 reference=APIHelper.SKIP,
                 delivery_date=APIHelper.SKIP,
                 dimension=APIHelper.SKIP,
                 address=APIHelper.SKIP,
                 product_options=APIHelper.SKIP,
                 status=APIHelper.SKIP):
        """Constructor for the Shipment11 class"""

        # Initialize members of the class
        if main_barcode is not APIHelper.SKIP:
            self.main_barcode = main_barcode 
        if barcode is not APIHelper.SKIP:
            self.barcode = barcode 
        if shipment_amount is not APIHelper.SKIP:
            self.shipment_amount = shipment_amount 
        if shipment_counter is not APIHelper.SKIP:
            self.shipment_counter = shipment_counter 
        if customer is not APIHelper.SKIP:
            self.customer = customer 
        if product_code is not APIHelper.SKIP:
            self.product_code = product_code 
        if product_description is not APIHelper.SKIP:
            self.product_description = product_description 
        if reference is not APIHelper.SKIP:
            self.reference = reference 
        if delivery_date is not APIHelper.SKIP:
            self.delivery_date = delivery_date 
        if dimension is not APIHelper.SKIP:
            self.dimension = dimension 
        if address is not APIHelper.SKIP:
            self.address = address 
        if product_options is not APIHelper.SKIP:
            self.product_options = product_options 
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
        main_barcode = dictionary.get("MainBarcode") if dictionary.get("MainBarcode") else APIHelper.SKIP
        barcode = dictionary.get("Barcode") if dictionary.get("Barcode") else APIHelper.SKIP
        shipment_amount = dictionary.get("ShipmentAmount") if dictionary.get("ShipmentAmount") else APIHelper.SKIP
        shipment_counter = dictionary.get("ShipmentCounter") if dictionary.get("ShipmentCounter") else APIHelper.SKIP
        customer = Customer2.from_dictionary(dictionary.get('Customer')) if 'Customer' in dictionary.keys() else APIHelper.SKIP
        product_code = dictionary.get("ProductCode") if dictionary.get("ProductCode") else APIHelper.SKIP
        product_description = dictionary.get("ProductDescription") if dictionary.get("ProductDescription") else APIHelper.SKIP
        reference = dictionary.get("Reference") if dictionary.get("Reference") else APIHelper.SKIP
        delivery_date = dictionary.get("DeliveryDate") if dictionary.get("DeliveryDate") else APIHelper.SKIP
        dimension = Dimension1.from_dictionary(dictionary.get('Dimension')) if 'Dimension' in dictionary.keys() else APIHelper.SKIP
        address = None
        if dictionary.get('Address') is not None:
            address = [Address4.from_dictionary(x) for x in dictionary.get('Address')]
        else:
            address = APIHelper.SKIP
        product_options = ProductOptions.from_dictionary(dictionary.get('ProductOptions')) if 'ProductOptions' in dictionary.keys() else APIHelper.SKIP
        status = Status.from_dictionary(dictionary.get('Status')) if 'Status' in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(main_barcode,
                   barcode,
                   shipment_amount,
                   shipment_counter,
                   customer,
                   product_code,
                   product_description,
                   reference,
                   delivery_date,
                   dimension,
                   address,
                   product_options,
                   status)
