# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper
from postnlecommerce.models.checkout_location import CheckoutLocation


class CheckoutPickupOption(object):

    """Implementation of the 'checkoutPickupOption' model.

    Attributes:
        pickup_date (str): Date from which the parcel can be picked up at the
            PostNL location
        shipping_date (str): The date when you need to deliver the shipment to
            PostNL to ensure the expected delivery date is achieved. Will be
            returned as 'null' if not calculated
        option (str): The pickup option
        locations (List[CheckoutLocation]): Array of pickup locations

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "pickup_date": 'PickupDate',
        "shipping_date": 'ShippingDate',
        "option": 'Option',
        "locations": 'Locations'
    }

    _optionals = [
        'pickup_date',
        'shipping_date',
        'option',
        'locations',
    ]

    def __init__(self,
                 pickup_date=APIHelper.SKIP,
                 shipping_date=APIHelper.SKIP,
                 option=APIHelper.SKIP,
                 locations=APIHelper.SKIP):
        """Constructor for the CheckoutPickupOption class"""

        # Initialize members of the class
        if pickup_date is not APIHelper.SKIP:
            self.pickup_date = pickup_date 
        if shipping_date is not APIHelper.SKIP:
            self.shipping_date = shipping_date 
        if option is not APIHelper.SKIP:
            self.option = option 
        if locations is not APIHelper.SKIP:
            self.locations = locations 

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
        pickup_date = dictionary.get("PickupDate") if dictionary.get("PickupDate") else APIHelper.SKIP
        shipping_date = dictionary.get("ShippingDate") if dictionary.get("ShippingDate") else APIHelper.SKIP
        option = dictionary.get("Option") if dictionary.get("Option") else APIHelper.SKIP
        locations = None
        if dictionary.get('Locations') is not None:
            locations = [CheckoutLocation.from_dictionary(x) for x in dictionary.get('Locations')]
        else:
            locations = APIHelper.SKIP
        # Return an object of this model
        return cls(pickup_date,
                   shipping_date,
                   option,
                   locations)

    def __repr__(self):
        return (f'{self.__class__.__name__}('
                f'pickup_date={(self.pickup_date if hasattr(self, "pickup_date") else None)!r}, '
                f'shipping_date={(self.shipping_date if hasattr(self, "shipping_date") else None)!r}, '
                f'option={(self.option if hasattr(self, "option") else None)!r}, '
                f'locations={(self.locations if hasattr(self, "locations") else None)!r})')

    def __str__(self):
        return (f'{self.__class__.__name__}('
                f'pickup_date={(self.pickup_date if hasattr(self, "pickup_date") else None)!s}, '
                f'shipping_date={(self.shipping_date if hasattr(self, "shipping_date") else None)!s}, '
                f'option={(self.option if hasattr(self, "option") else None)!s}, '
                f'locations={(self.locations if hasattr(self, "locations") else None)!s})')
