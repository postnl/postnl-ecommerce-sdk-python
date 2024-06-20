# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper
from postnlecommerce.models.complete_status import CompleteStatus
from postnlecommerce.models.current_status import CurrentStatus
from postnlecommerce.models.shippingstatus_warning import ShippingstatusWarning


class ShippingstatusResponse(object):

    """Implementation of the 'shippingstatusResponse' model.

    TODO: type model description here.

    Attributes:
        complete_status (CompleteStatus): The current status and old statuses
            of the shipment
        current_status (CurrentStatus): The current status and old statuses of
            the shipment
        warnings (List[ShippingstatusWarning]): Possible warnings (see [Error
            Codes](https://developer.postnl.nl/docs/#/http/reference-data/error
            -codes) for possible values)

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "complete_status": 'CompleteStatus',
        "current_status": 'CurrentStatus',
        "warnings": 'Warnings'
    }

    _optionals = [
        'complete_status',
        'current_status',
        'warnings',
    ]

    def __init__(self,
                 complete_status=APIHelper.SKIP,
                 current_status=APIHelper.SKIP,
                 warnings=APIHelper.SKIP):
        """Constructor for the ShippingstatusResponse class"""

        # Initialize members of the class
        if complete_status is not APIHelper.SKIP:
            self.complete_status = complete_status 
        if current_status is not APIHelper.SKIP:
            self.current_status = current_status 
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
        complete_status = CompleteStatus.from_dictionary(dictionary.get('CompleteStatus')) if 'CompleteStatus' in dictionary.keys() else APIHelper.SKIP
        current_status = CurrentStatus.from_dictionary(dictionary.get('CurrentStatus')) if 'CurrentStatus' in dictionary.keys() else APIHelper.SKIP
        warnings = None
        if dictionary.get('Warnings') is not None:
            warnings = [ShippingstatusWarning.from_dictionary(x) for x in dictionary.get('Warnings')]
        else:
            warnings = APIHelper.SKIP
        # Return an object of this model
        return cls(complete_status,
                   current_status,
                   warnings)
