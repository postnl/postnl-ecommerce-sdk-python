# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper


class Contact(object):

    """Implementation of the 'Contact' model.

    TODO: type model description here.

    Attributes:
        contact_type (str): Type of the contact. This is a code. Please refer
            to the available [Contact
            types](https://developer.postnl.nl/docs/#/http/reference-data/refer
            ence-codes/contact-types) for the possible values.
        email (str): Email address of the contact. Mandatory in some cases.
            Either the Email or Telnr needs to be filled in for Non EU
            destinations. Please see
            [Guidelines](https://developer.postnl.nl/docs/#/http/api-endpoints/
            send-track/confirming/guidelines).
        sms_nr (str): Mobile phone number of the contact. Mandatory in some
            cases. Please see
            [Guidelines](https://developer.postnl.nl/docs/#/http/api-endpoints/
            send-track/confirming/guidelines).
        tel_nr (str): Phone number of the contact. Either the Email or Telnr
            needs to be filled in for Non EU destinations. Preferably prefixed
            with “+” and the international dialling code.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "contact_type": 'ContactType',
        "email": 'Email',
        "sms_nr": 'SMSNr',
        "tel_nr": 'TelNr'
    }

    _optionals = [
        'email',
        'sms_nr',
        'tel_nr',
    ]

    def __init__(self,
                 contact_type=None,
                 email=APIHelper.SKIP,
                 sms_nr=APIHelper.SKIP,
                 tel_nr=APIHelper.SKIP):
        """Constructor for the Contact class"""

        # Initialize members of the class
        self.contact_type = contact_type 
        if email is not APIHelper.SKIP:
            self.email = email 
        if sms_nr is not APIHelper.SKIP:
            self.sms_nr = sms_nr 
        if tel_nr is not APIHelper.SKIP:
            self.tel_nr = tel_nr 

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
        contact_type = dictionary.get("ContactType") if dictionary.get("ContactType") else None
        email = dictionary.get("Email") if dictionary.get("Email") else APIHelper.SKIP
        sms_nr = dictionary.get("SMSNr") if dictionary.get("SMSNr") else APIHelper.SKIP
        tel_nr = dictionary.get("TelNr") if dictionary.get("TelNr") else APIHelper.SKIP
        # Return an object of this model
        return cls(contact_type,
                   email,
                   sms_nr,
                   tel_nr)
