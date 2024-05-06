# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper


class Amount(object):

    """Implementation of the 'Amount' model.

    TODO: type model description here.

    Attributes:
        amount_type (str): Amount type. Please see [Amount
            types](https://developer.postnl.nl/docs/#/http/reference-data/refer
            ence-codes/amount-types) for the available types.
        account_name (str): Name of bank account owner
        bic (str): BIC number,optional for COD shipments (mandatory for bank
            account number other than originating in The Netherlands)
        currency (str): Currency code. only EUR, GBP, USD and CNY are
            allowed.
        iban (str): IBAN bank account number,mandatory for COD shipments.
            Dutch IBAN numbers are 18 characters
        reference (str): Personal payment reference
        transaction_number (str): Transaction number
        value (float): Money value in EUR (unless value Currency is specified
            for another currency). Value format (N6.2): #####0.00 (2 digits
            behind decimal dot). Mandatory for COD, Insured products (with the
            exception of certain productcodes with a standard insured
            amount).

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "amount_type": 'AmountType',
        "value": 'Value',
        "account_name": 'AccountName',
        "bic": 'BIC',
        "currency": 'Currency',
        "iban": 'IBAN',
        "reference": 'Reference',
        "transaction_number": 'TransactionNumber'
    }

    _optionals = [
        'account_name',
        'bic',
        'currency',
        'iban',
        'reference',
        'transaction_number',
    ]

    def __init__(self,
                 amount_type=None,
                 value=None,
                 account_name=APIHelper.SKIP,
                 bic=APIHelper.SKIP,
                 currency=APIHelper.SKIP,
                 iban=APIHelper.SKIP,
                 reference=APIHelper.SKIP,
                 transaction_number=APIHelper.SKIP):
        """Constructor for the Amount class"""

        # Initialize members of the class
        self.amount_type = amount_type 
        if account_name is not APIHelper.SKIP:
            self.account_name = account_name 
        if bic is not APIHelper.SKIP:
            self.bic = bic 
        if currency is not APIHelper.SKIP:
            self.currency = currency 
        if iban is not APIHelper.SKIP:
            self.iban = iban 
        if reference is not APIHelper.SKIP:
            self.reference = reference 
        if transaction_number is not APIHelper.SKIP:
            self.transaction_number = transaction_number 
        self.value = value 

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
        amount_type = dictionary.get("AmountType") if dictionary.get("AmountType") else None
        value = dictionary.get("Value") if dictionary.get("Value") else None
        account_name = dictionary.get("AccountName") if dictionary.get("AccountName") else APIHelper.SKIP
        bic = dictionary.get("BIC") if dictionary.get("BIC") else APIHelper.SKIP
        currency = dictionary.get("Currency") if dictionary.get("Currency") else APIHelper.SKIP
        iban = dictionary.get("IBAN") if dictionary.get("IBAN") else APIHelper.SKIP
        reference = dictionary.get("Reference") if dictionary.get("Reference") else APIHelper.SKIP
        transaction_number = dictionary.get("TransactionNumber") if dictionary.get("TransactionNumber") else APIHelper.SKIP
        # Return an object of this model
        return cls(amount_type,
                   value,
                   account_name,
                   bic,
                   currency,
                   iban,
                   reference,
                   transaction_number)
