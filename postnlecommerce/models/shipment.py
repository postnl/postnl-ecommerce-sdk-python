# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper
from postnlecommerce.models.address_11 import Address11
from postnlecommerce.models.amount import Amount
from postnlecommerce.models.contact import Contact
from postnlecommerce.models.custom import Custom
from postnlecommerce.models.dimension import Dimension
from postnlecommerce.models.group import Group
from postnlecommerce.models.hazardous_material import HazardousMaterial
from postnlecommerce.models.product_option import ProductOption


class Shipment(object):

    """Implementation of the 'Shipment' model.

    TODO: type model description here.

    Attributes:
        addresses (List[Address11]): List of 1 or more Address type elements.
            At least 1 address type is mandatory. See [Address
            types](#tag/Reference-codes/Address-types) for the available
            types.
        amounts (List[Amount]): List of amount types. An amount represents a
            value of the shipment. Amount type 01 mandatory for COD-shipments,
            Amount type 02 mandatory for domestic insured shipments. Please
            see [Amount types](#tag/Reference-codes/Amount-types) for the
            available types.
        barcode (str): Barcode of the shipment. This is a unique value. Note:
            If you leave this attribute out of your request an unique barcode
            will be generated automatically.
        coding_text (str): Code used for logistic purposes (usually generated
            by the service itself and returned in the response). Please note
            that this must be provided when  using the Confirm API to confirm
            shipments where coding texts are required (e.g. letterbox
            parcels).
        collection_time_stamp_start (str): Starting date/time of the
            collection of the shipment. Format: dd-MM-yyyy hh:mm:ss
        collection_time_stamp_end (str): Ending date/time of the collection of
            the shipment. Format: dd-MM-yyyy hh:mm:ss
        contacts (List[Contact]): One or more ContactType elements belonging
            to a shipment. Mandatory in some cases. Please refer to the
            available [Contact types](#tag/Reference-codes/Contact-types) for
            the possible values.
        content (str): Content of the shipment. Mandatory for Extra@Home
            shipments
        cost_center (str): Cost center of the shipment. This value will appear
            on your invoice
        customer_order_number (str): Order number of the customer
        customs (List[Custom]): The Customs type is mandatory for non-EU
            shipments and not allowed for any other shipment types.
        delivery_address (str): Delivery address specification. This field is
            mandatory when AddressType on the Address is 09.
        delivery_date (str): Mandatory when using Mailbox Parcels (for
            generation of the coding rule) and delivery options like
            Evening/Morning/Sameday delivery etc.
        dimension (Dimension): Note: Length, Width, Height values are about
            the order of the size and need to be filled in from the longest to
            the shortest value. For example: shipment’s official height is
            700mm, width 500mm, length 300mm. The longest side (highest value)
            of 700mm needs to be entered at Length. Width value becomes 500mm,
            Height value: 300mm (the lowest). Entering the dimensions in the
            wrong order may result in incorrect shipping labels and longer
            delivery times. The maximum dimensions can be found in your PostNL
            contract.
        down_partner_barcode (str): Barcode of the downstream network partner
            of PostNL Parcels. Madatory for requesting Parcels Non-EU
            combilabel product codes.
        down_partner_id (str): Identification of the downstream network
            partner of PostNL Pakketten.
        down_partner_location (str): Identification of the location of the
            downstream network partner of PostNL Pakketten.
        groups (List[Group]): List of 0 or more Group types with data,
            grouping multiple shipments together. Mandatory for multicollo
            shipments. Please see
            [Guidelines](https://developer.postnl.nl/browse-apis/send-and-track
            /labelling-webservice/) (Multiple shipments) for more
            information.
        hazardous_material (List[HazardousMaterial]): Array of hazardous
            materials contained in the shipment
        product_code_collect (str): Deprecated. Collection product code of a
            shipment.
        product_code_delivery (str): Product code of the shipment. See the
            [Products page](#tag/Product-codes) for possible products.
        product_options (List[ProductOption]): Product options for the
            shipment, mandatory for certain products, see the [Products
            page](#tag/Product-codes).
        receiver_date_of_birth (str): Date of birth. Mandatory for Age check
            products
        reference (str): Your own reference of the shipment. Mandatory for
            Extra@Home shipments; for E@H this is used to create your order
            number, so this should be unique for each request.
        reference_collect (str): Additional reference of the collect order of
            the shipment
        remark (str): Remark of the shipment.
        return_barcode (str): Return barcode of the shipment. PostNL will
            provide you with a separate customer code specifically for
            generating the returnBarcode. Mandatory for Label in the Box
            (return label) shipments.
        return_reference (str): Return reference of the shipment
        timeslot_id (str): Deprecated. ID of the chosen timeslot as returned
            by the timeslot webservice

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "addresses": 'Addresses',
        "barcode": 'Barcode',
        "dimension": 'Dimension',
        "product_code_delivery": 'ProductCodeDelivery',
        "amounts": 'Amounts',
        "coding_text": 'CodingText',
        "collection_time_stamp_start": 'CollectionTimeStampStart',
        "collection_time_stamp_end": 'CollectionTimeStampEnd',
        "contacts": 'Contacts',
        "content": 'Content',
        "cost_center": 'CostCenter',
        "customer_order_number": 'CustomerOrderNumber',
        "customs": 'Customs',
        "delivery_address": 'DeliveryAddress',
        "delivery_date": 'DeliveryDate',
        "down_partner_barcode": 'DownPartnerBarcode',
        "down_partner_id": 'DownPartnerID',
        "down_partner_location": 'DownPartnerLocation',
        "groups": 'Groups',
        "hazardous_material": 'HazardousMaterial',
        "product_code_collect": 'ProductCodeCollect',
        "product_options": 'ProductOptions',
        "receiver_date_of_birth": 'ReceiverDateOfBirth',
        "reference": 'Reference',
        "reference_collect": 'ReferenceCollect',
        "remark": 'Remark',
        "return_barcode": 'ReturnBarcode',
        "return_reference": 'ReturnReference',
        "timeslot_id": 'TimeslotID'
    }

    _optionals = [
        'amounts',
        'coding_text',
        'collection_time_stamp_start',
        'collection_time_stamp_end',
        'contacts',
        'content',
        'cost_center',
        'customer_order_number',
        'customs',
        'delivery_address',
        'delivery_date',
        'down_partner_barcode',
        'down_partner_id',
        'down_partner_location',
        'groups',
        'hazardous_material',
        'product_code_collect',
        'product_options',
        'receiver_date_of_birth',
        'reference',
        'reference_collect',
        'remark',
        'return_barcode',
        'return_reference',
        'timeslot_id',
    ]

    def __init__(self,
                 addresses=None,
                 barcode=None,
                 dimension=None,
                 product_code_delivery='3085',
                 amounts=APIHelper.SKIP,
                 coding_text=APIHelper.SKIP,
                 collection_time_stamp_start=APIHelper.SKIP,
                 collection_time_stamp_end=APIHelper.SKIP,
                 contacts=APIHelper.SKIP,
                 content=APIHelper.SKIP,
                 cost_center=APIHelper.SKIP,
                 customer_order_number=APIHelper.SKIP,
                 customs=APIHelper.SKIP,
                 delivery_address=APIHelper.SKIP,
                 delivery_date=APIHelper.SKIP,
                 down_partner_barcode=APIHelper.SKIP,
                 down_partner_id=APIHelper.SKIP,
                 down_partner_location=APIHelper.SKIP,
                 groups=APIHelper.SKIP,
                 hazardous_material=APIHelper.SKIP,
                 product_code_collect=APIHelper.SKIP,
                 product_options=APIHelper.SKIP,
                 receiver_date_of_birth=APIHelper.SKIP,
                 reference=APIHelper.SKIP,
                 reference_collect=APIHelper.SKIP,
                 remark=APIHelper.SKIP,
                 return_barcode=APIHelper.SKIP,
                 return_reference=APIHelper.SKIP,
                 timeslot_id=APIHelper.SKIP):
        """Constructor for the Shipment class"""

        # Initialize members of the class
        self.addresses = addresses 
        if amounts is not APIHelper.SKIP:
            self.amounts = amounts 
        self.barcode = barcode 
        if coding_text is not APIHelper.SKIP:
            self.coding_text = coding_text 
        if collection_time_stamp_start is not APIHelper.SKIP:
            self.collection_time_stamp_start = collection_time_stamp_start 
        if collection_time_stamp_end is not APIHelper.SKIP:
            self.collection_time_stamp_end = collection_time_stamp_end 
        if contacts is not APIHelper.SKIP:
            self.contacts = contacts 
        if content is not APIHelper.SKIP:
            self.content = content 
        if cost_center is not APIHelper.SKIP:
            self.cost_center = cost_center 
        if customer_order_number is not APIHelper.SKIP:
            self.customer_order_number = customer_order_number 
        if customs is not APIHelper.SKIP:
            self.customs = customs 
        if delivery_address is not APIHelper.SKIP:
            self.delivery_address = delivery_address 
        if delivery_date is not APIHelper.SKIP:
            self.delivery_date = delivery_date 
        self.dimension = dimension 
        if down_partner_barcode is not APIHelper.SKIP:
            self.down_partner_barcode = down_partner_barcode 
        if down_partner_id is not APIHelper.SKIP:
            self.down_partner_id = down_partner_id 
        if down_partner_location is not APIHelper.SKIP:
            self.down_partner_location = down_partner_location 
        if groups is not APIHelper.SKIP:
            self.groups = groups 
        if hazardous_material is not APIHelper.SKIP:
            self.hazardous_material = hazardous_material 
        if product_code_collect is not APIHelper.SKIP:
            self.product_code_collect = product_code_collect 
        self.product_code_delivery = product_code_delivery 
        if product_options is not APIHelper.SKIP:
            self.product_options = product_options 
        if receiver_date_of_birth is not APIHelper.SKIP:
            self.receiver_date_of_birth = receiver_date_of_birth 
        if reference is not APIHelper.SKIP:
            self.reference = reference 
        if reference_collect is not APIHelper.SKIP:
            self.reference_collect = reference_collect 
        if remark is not APIHelper.SKIP:
            self.remark = remark 
        if return_barcode is not APIHelper.SKIP:
            self.return_barcode = return_barcode 
        if return_reference is not APIHelper.SKIP:
            self.return_reference = return_reference 
        if timeslot_id is not APIHelper.SKIP:
            self.timeslot_id = timeslot_id 

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
        addresses = None
        if dictionary.get('Addresses') is not None:
            addresses = [Address11.from_dictionary(x) for x in dictionary.get('Addresses')]
        barcode = dictionary.get("Barcode") if dictionary.get("Barcode") else None
        dimension = Dimension.from_dictionary(dictionary.get('Dimension')) if dictionary.get('Dimension') else None
        product_code_delivery = dictionary.get("ProductCodeDelivery") if dictionary.get("ProductCodeDelivery") else '3085'
        amounts = None
        if dictionary.get('Amounts') is not None:
            amounts = [Amount.from_dictionary(x) for x in dictionary.get('Amounts')]
        else:
            amounts = APIHelper.SKIP
        coding_text = dictionary.get("CodingText") if dictionary.get("CodingText") else APIHelper.SKIP
        collection_time_stamp_start = dictionary.get("CollectionTimeStampStart") if dictionary.get("CollectionTimeStampStart") else APIHelper.SKIP
        collection_time_stamp_end = dictionary.get("CollectionTimeStampEnd") if dictionary.get("CollectionTimeStampEnd") else APIHelper.SKIP
        contacts = None
        if dictionary.get('Contacts') is not None:
            contacts = [Contact.from_dictionary(x) for x in dictionary.get('Contacts')]
        else:
            contacts = APIHelper.SKIP
        content = dictionary.get("Content") if dictionary.get("Content") else APIHelper.SKIP
        cost_center = dictionary.get("CostCenter") if dictionary.get("CostCenter") else APIHelper.SKIP
        customer_order_number = dictionary.get("CustomerOrderNumber") if dictionary.get("CustomerOrderNumber") else APIHelper.SKIP
        customs = None
        if dictionary.get('Customs') is not None:
            customs = [Custom.from_dictionary(x) for x in dictionary.get('Customs')]
        else:
            customs = APIHelper.SKIP
        delivery_address = dictionary.get("DeliveryAddress") if dictionary.get("DeliveryAddress") else APIHelper.SKIP
        delivery_date = dictionary.get("DeliveryDate") if dictionary.get("DeliveryDate") else APIHelper.SKIP
        down_partner_barcode = dictionary.get("DownPartnerBarcode") if dictionary.get("DownPartnerBarcode") else APIHelper.SKIP
        down_partner_id = dictionary.get("DownPartnerID") if dictionary.get("DownPartnerID") else APIHelper.SKIP
        down_partner_location = dictionary.get("DownPartnerLocation") if dictionary.get("DownPartnerLocation") else APIHelper.SKIP
        groups = None
        if dictionary.get('Groups') is not None:
            groups = [Group.from_dictionary(x) for x in dictionary.get('Groups')]
        else:
            groups = APIHelper.SKIP
        hazardous_material = None
        if dictionary.get('HazardousMaterial') is not None:
            hazardous_material = [HazardousMaterial.from_dictionary(x) for x in dictionary.get('HazardousMaterial')]
        else:
            hazardous_material = APIHelper.SKIP
        product_code_collect = dictionary.get("ProductCodeCollect") if dictionary.get("ProductCodeCollect") else APIHelper.SKIP
        product_options = None
        if dictionary.get('ProductOptions') is not None:
            product_options = [ProductOption.from_dictionary(x) for x in dictionary.get('ProductOptions')]
        else:
            product_options = APIHelper.SKIP
        receiver_date_of_birth = dictionary.get("ReceiverDateOfBirth") if dictionary.get("ReceiverDateOfBirth") else APIHelper.SKIP
        reference = dictionary.get("Reference") if dictionary.get("Reference") else APIHelper.SKIP
        reference_collect = dictionary.get("ReferenceCollect") if dictionary.get("ReferenceCollect") else APIHelper.SKIP
        remark = dictionary.get("Remark") if dictionary.get("Remark") else APIHelper.SKIP
        return_barcode = dictionary.get("ReturnBarcode") if dictionary.get("ReturnBarcode") else APIHelper.SKIP
        return_reference = dictionary.get("ReturnReference") if dictionary.get("ReturnReference") else APIHelper.SKIP
        timeslot_id = dictionary.get("TimeslotID") if dictionary.get("TimeslotID") else APIHelper.SKIP
        # Return an object of this model
        return cls(addresses,
                   barcode,
                   dimension,
                   product_code_delivery,
                   amounts,
                   coding_text,
                   collection_time_stamp_start,
                   collection_time_stamp_end,
                   contacts,
                   content,
                   cost_center,
                   customer_order_number,
                   customs,
                   delivery_address,
                   delivery_date,
                   down_partner_barcode,
                   down_partner_id,
                   down_partner_location,
                   groups,
                   hazardous_material,
                   product_code_collect,
                   product_options,
                   receiver_date_of_birth,
                   reference,
                   reference_collect,
                   remark,
                   return_barcode,
                   return_reference,
                   timeslot_id)
