# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper
from postnlecommerce.models.labelling_customs_content import LabellingCustomsContent


class Customs(object):

    """Implementation of the 'Customs' model.

    The Customs type is mandatory for non-EU shipments and not allowed for any
    other shipment types.

    Attributes:
        certificate (bool): Fill in if applicable, for specific items a export
            certificate is obliged, as proof that the item complies to the
            sanity regulations, [more
            information](https://ondernemersplein.kvk.nl/fytosanitair-of-veteri
            nair-exportcertificaat-aanvragen/). Mandatory for Parcel shipments
            in the category type Commercial Goods, Commercial Sample and
            Returned Goods (Certificate, Invoice or License; at least 1 out of
            3 must be selected)
        certificate_nr (str): Mandatory when Certificate is true.
        license (bool): Fill in if applicable. Mandatory for Parcel shipments
            in the category type Commercial Goods, Commercial Sample and
            Returned Goods (Certificate, Invoice or License; at least 1 out of
            3 must be selected).
        license_nr (str): Mandatory when License is true.
        invoice (bool): Fill in the invoice number of the shipment. For a
            faster customs clearing process apply the invoice on the outside
            of the shipment. Mandatory for Parcel shipments in the category
            type Commercial Goods, Commercial Sample and Returned Goods
            (Certificate, Invoice or License; at least 1 out of 3 must be
            selected).
        invoice_nr (str): Mandatory when Invoice is true
        handle_as_non_deliverable (bool): Determines what to do when the
            shipment cannot be delivered the first time (if this is set to
            true,the shipment will be returned after the first failed attempt)
        currency (CurrencyLabellingAPIEnum): Currency code,only EUR and USS
            are allowed
        shipment_type (ShipmentTypeEnum): Type of shipment,possible values:
            Gift,Documents,Commercial Goods,Commercial Sample,Returned Goods
        trusted_shipper_id (str): 'Use only when available. Depending on the
            destination with this ID the customs process can be faster. Only
            fill in this customs reference number if the sender is registrated
            as Trusted Shipper in the country of destination'
        importer_reference_code (str): Importer reference code. Fill in a Tax
            Code or VAT number or Importer code. Depending on the destination
            with this reference the customs process can be faster.
        transaction_code (str): Code and accompanying description according to
            UPU Codelist 136. Codes to be used are shown below for your
            reference. Or see the [Reference
            data](https://developer.postnl.nl/docs/#/http/reference-data/refere
            nce-codes/transaction-codes).
        transaction_description (str): Transaction description; see
            [here](https://developer.postnl.nl/docs/#/http/reference-data/refer
            ence-codes/transaction-codes) for common examples.
        content (List[LabellingCustomsContent]): The contents of the shipment.
            This section is mandatory (minimum once, maximum 5).

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "currency": 'Currency',
        "shipment_type": 'ShipmentType',
        "content": 'Content',
        "certificate": 'Certificate',
        "certificate_nr": 'CertificateNr',
        "license": 'License',
        "license_nr": 'LicenseNr',
        "invoice": 'Invoice',
        "invoice_nr": 'InvoiceNr',
        "handle_as_non_deliverable": 'HandleAsNonDeliverable',
        "trusted_shipper_id": 'TrustedShipperID',
        "importer_reference_code": 'ImporterReferenceCode',
        "transaction_code": 'TransactionCode',
        "transaction_description": 'TransactionDescription'
    }

    _optionals = [
        'certificate',
        'certificate_nr',
        'license',
        'license_nr',
        'invoice',
        'invoice_nr',
        'handle_as_non_deliverable',
        'trusted_shipper_id',
        'importer_reference_code',
        'transaction_code',
        'transaction_description',
    ]

    def __init__(self,
                 currency=None,
                 shipment_type=None,
                 content=None,
                 certificate=APIHelper.SKIP,
                 certificate_nr=APIHelper.SKIP,
                 license=APIHelper.SKIP,
                 license_nr=APIHelper.SKIP,
                 invoice=APIHelper.SKIP,
                 invoice_nr=APIHelper.SKIP,
                 handle_as_non_deliverable=APIHelper.SKIP,
                 trusted_shipper_id=APIHelper.SKIP,
                 importer_reference_code=APIHelper.SKIP,
                 transaction_code=APIHelper.SKIP,
                 transaction_description=APIHelper.SKIP):
        """Constructor for the Customs class"""

        # Initialize members of the class
        if certificate is not APIHelper.SKIP:
            self.certificate = certificate 
        if certificate_nr is not APIHelper.SKIP:
            self.certificate_nr = certificate_nr 
        if license is not APIHelper.SKIP:
            self.license = license 
        if license_nr is not APIHelper.SKIP:
            self.license_nr = license_nr 
        if invoice is not APIHelper.SKIP:
            self.invoice = invoice 
        if invoice_nr is not APIHelper.SKIP:
            self.invoice_nr = invoice_nr 
        if handle_as_non_deliverable is not APIHelper.SKIP:
            self.handle_as_non_deliverable = handle_as_non_deliverable 
        self.currency = currency 
        self.shipment_type = shipment_type 
        if trusted_shipper_id is not APIHelper.SKIP:
            self.trusted_shipper_id = trusted_shipper_id 
        if importer_reference_code is not APIHelper.SKIP:
            self.importer_reference_code = importer_reference_code 
        if transaction_code is not APIHelper.SKIP:
            self.transaction_code = transaction_code 
        if transaction_description is not APIHelper.SKIP:
            self.transaction_description = transaction_description 
        self.content = content 

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

        if not isinstance(dictionary, dict) or dictionary is None:
            return None

        # Extract variables from the dictionary
        currency = dictionary.get("Currency") if dictionary.get("Currency") else None
        shipment_type = dictionary.get("ShipmentType") if dictionary.get("ShipmentType") else None
        content = None
        if dictionary.get('Content') is not None:
            content = [LabellingCustomsContent.from_dictionary(x) for x in dictionary.get('Content')]
        certificate = dictionary.get("Certificate") if "Certificate" in dictionary.keys() else APIHelper.SKIP
        certificate_nr = dictionary.get("CertificateNr") if dictionary.get("CertificateNr") else APIHelper.SKIP
        license = dictionary.get("License") if "License" in dictionary.keys() else APIHelper.SKIP
        license_nr = dictionary.get("LicenseNr") if dictionary.get("LicenseNr") else APIHelper.SKIP
        invoice = dictionary.get("Invoice") if "Invoice" in dictionary.keys() else APIHelper.SKIP
        invoice_nr = dictionary.get("InvoiceNr") if dictionary.get("InvoiceNr") else APIHelper.SKIP
        handle_as_non_deliverable = dictionary.get("HandleAsNonDeliverable") if "HandleAsNonDeliverable" in dictionary.keys() else APIHelper.SKIP
        trusted_shipper_id = dictionary.get("TrustedShipperID") if dictionary.get("TrustedShipperID") else APIHelper.SKIP
        importer_reference_code = dictionary.get("ImporterReferenceCode") if dictionary.get("ImporterReferenceCode") else APIHelper.SKIP
        transaction_code = dictionary.get("TransactionCode") if dictionary.get("TransactionCode") else APIHelper.SKIP
        transaction_description = dictionary.get("TransactionDescription") if dictionary.get("TransactionDescription") else APIHelper.SKIP
        # Return an object of this model
        return cls(currency,
                   shipment_type,
                   content,
                   certificate,
                   certificate_nr,
                   license,
                   license_nr,
                   invoice,
                   invoice_nr,
                   handle_as_non_deliverable,
                   trusted_shipper_id,
                   importer_reference_code,
                   transaction_code,
                   transaction_description)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'certificate={(self.certificate if hasattr(self, "certificate") else None)!r}, '
                f'certificate_nr={(self.certificate_nr if hasattr(self, "certificate_nr") else None)!r}, '
                f'license={(self.license if hasattr(self, "license") else None)!r}, '
                f'license_nr={(self.license_nr if hasattr(self, "license_nr") else None)!r}, '
                f'invoice={(self.invoice if hasattr(self, "invoice") else None)!r}, '
                f'invoice_nr={(self.invoice_nr if hasattr(self, "invoice_nr") else None)!r}, '
                f'handle_as_non_deliverable={(self.handle_as_non_deliverable if hasattr(self, "handle_as_non_deliverable") else None)!r}, '
                f'currency={self.currency!r}, '
                f'shipment_type={self.shipment_type!r}, '
                f'trusted_shipper_id={(self.trusted_shipper_id if hasattr(self, "trusted_shipper_id") else None)!r}, '
                f'importer_reference_code={(self.importer_reference_code if hasattr(self, "importer_reference_code") else None)!r}, '
                f'transaction_code={(self.transaction_code if hasattr(self, "transaction_code") else None)!r}, '
                f'transaction_description={(self.transaction_description if hasattr(self, "transaction_description") else None)!r}, '
                f'content={self.content!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'certificate={(self.certificate if hasattr(self, "certificate") else None)!s}, '
                f'certificate_nr={(self.certificate_nr if hasattr(self, "certificate_nr") else None)!s}, '
                f'license={(self.license if hasattr(self, "license") else None)!s}, '
                f'license_nr={(self.license_nr if hasattr(self, "license_nr") else None)!s}, '
                f'invoice={(self.invoice if hasattr(self, "invoice") else None)!s}, '
                f'invoice_nr={(self.invoice_nr if hasattr(self, "invoice_nr") else None)!s}, '
                f'handle_as_non_deliverable={(self.handle_as_non_deliverable if hasattr(self, "handle_as_non_deliverable") else None)!s}, '
                f'currency={self.currency!s}, '
                f'shipment_type={self.shipment_type!s}, '
                f'trusted_shipper_id={(self.trusted_shipper_id if hasattr(self, "trusted_shipper_id") else None)!s}, '
                f'importer_reference_code={(self.importer_reference_code if hasattr(self, "importer_reference_code") else None)!s}, '
                f'transaction_code={(self.transaction_code if hasattr(self, "transaction_code") else None)!s}, '
                f'transaction_description={(self.transaction_description if hasattr(self, "transaction_description") else None)!s}, '
                f'content={self.content!s})')
