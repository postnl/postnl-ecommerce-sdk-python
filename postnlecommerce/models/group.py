# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper


class Group(object):

    """Implementation of the 'Group' model.

    TODO: type model description here.

    Attributes:
        group_type (str): Group sort that determines the type of group that is
            indicated. This is a code. For possible values, please see
            [here](https://developer.postnl.nl/docs/#/http/reference-data/refer
            ence-codes/group-types)
        group_sequence (int): Sequence number of the collo within the complete
            shipment (e.g. collo 2 of 4) Mandatory for multicollo shipments
        group_count (int): Total number of colli in the shipment (in case of
            multicolli shipments) Mandatory for multicollo shipments
        main_barcode (str): Main barcode for the shipment (in case of
            multicolli shipments) Mandatory for multicollo shipments

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "group_type": 'GroupType',
        "main_barcode": 'MainBarcode',
        "group_sequence": 'GroupSequence',
        "group_count": 'GroupCount'
    }

    _optionals = [
        'group_sequence',
        'group_count',
    ]

    def __init__(self,
                 group_type=None,
                 main_barcode=None,
                 group_sequence=APIHelper.SKIP,
                 group_count=APIHelper.SKIP):
        """Constructor for the Group class"""

        # Initialize members of the class
        self.group_type = group_type 
        if group_sequence is not APIHelper.SKIP:
            self.group_sequence = group_sequence 
        if group_count is not APIHelper.SKIP:
            self.group_count = group_count 
        self.main_barcode = main_barcode 

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
        group_type = dictionary.get("GroupType") if dictionary.get("GroupType") else None
        main_barcode = dictionary.get("MainBarcode") if dictionary.get("MainBarcode") else None
        group_sequence = dictionary.get("GroupSequence") if dictionary.get("GroupSequence") else APIHelper.SKIP
        group_count = dictionary.get("GroupCount") if dictionary.get("GroupCount") else APIHelper.SKIP
        # Return an object of this model
        return cls(group_type,
                   main_barcode,
                   group_sequence,
                   group_count)
