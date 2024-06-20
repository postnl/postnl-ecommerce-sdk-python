# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper
from postnlecommerce.models.checkout_delivery_option import CheckoutDeliveryOption
from postnlecommerce.models.checkout_pickup_option import CheckoutPickupOption
from postnlecommerce.models.checkout_warning import CheckoutWarning


class CheckoutResponse(object):

    """Implementation of the 'checkoutResponse' model.

    TODO: type model description here.

    Attributes:
        delivery_options (List[CheckoutDeliveryOption]): Array of delivery
            options
        pickup_options (List[CheckoutPickupOption]): Array of possible pickup
            options
        warnings (List[CheckoutWarning]): An array of warnings

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "delivery_options": 'DeliveryOptions',
        "pickup_options": 'PickupOptions',
        "warnings": 'Warnings'
    }

    _optionals = [
        'delivery_options',
        'pickup_options',
        'warnings',
    ]

    def __init__(self,
                 delivery_options=APIHelper.SKIP,
                 pickup_options=APIHelper.SKIP,
                 warnings=APIHelper.SKIP):
        """Constructor for the CheckoutResponse class"""

        # Initialize members of the class
        if delivery_options is not APIHelper.SKIP:
            self.delivery_options = delivery_options 
        if pickup_options is not APIHelper.SKIP:
            self.pickup_options = pickup_options 
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
        delivery_options = None
        if dictionary.get('DeliveryOptions') is not None:
            delivery_options = [CheckoutDeliveryOption.from_dictionary(x) for x in dictionary.get('DeliveryOptions')]
        else:
            delivery_options = APIHelper.SKIP
        pickup_options = None
        if dictionary.get('PickupOptions') is not None:
            pickup_options = [CheckoutPickupOption.from_dictionary(x) for x in dictionary.get('PickupOptions')]
        else:
            pickup_options = APIHelper.SKIP
        warnings = None
        if dictionary.get('Warnings') is not None:
            warnings = [CheckoutWarning.from_dictionary(x) for x in dictionary.get('Warnings')]
        else:
            warnings = APIHelper.SKIP
        # Return an object of this model
        return cls(delivery_options,
                   pickup_options,
                   warnings)
