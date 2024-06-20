# -*- coding: utf-8 -*-

"""
postnlecommerce

This file was automatically generated for PostNL by APIMATIC v3.0 (
 https://www.apimatic.io ).
"""
from postnlecommerce.api_helper import APIHelper
from postnlecommerce.models.checkout_address import CheckoutAddress
from postnlecommerce.models.checkout_cut_off_time import CheckoutCutOffTime


class CheckoutRequest(object):

    """Implementation of the 'checkoutRequest' model.

    TODO: type model description here.

    Attributes:
        order_date (str): The order date of the shipment. Format dd-MM-YYYY
            HH:mm:ss
        shipping_duration (int): The amount of days it takes for a parcel to
            be received by PostN. If you delivery the parcel the same day as
            the order is placed on the webshop, please use the value of 1. A
            value of 2 means the parcel will arrive at PostNL a day later
            etc.
        cut_off_times (List[CheckoutCutOffTime]): Array of CutOffTimes
        holiday_sorting (bool): Specifies whether you are available to ship
            parcels to PostNL during holidays
        options (List[CheckoutOptionEnum]): Specifies the delivery and pickup
            options.
        locations (int): Specifies the number of locations you want returned.
            This can be a value of 1-3
        days (int): Specifies the number of days for which the timeframes are
            returned. This can be a value of 1-9
        addresses (List[CheckoutAddress]): Array of addresses

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "order_date": 'OrderDate',
        "cut_off_times": 'CutOffTimes',
        "options": 'Options',
        "locations": 'Locations',
        "days": 'Days',
        "addresses": 'Addresses',
        "shipping_duration": 'ShippingDuration',
        "holiday_sorting": 'HolidaySorting'
    }

    _optionals = [
        'shipping_duration',
        'holiday_sorting',
    ]

    def __init__(self,
                 order_date=None,
                 cut_off_times=None,
                 options=None,
                 locations=None,
                 days=None,
                 addresses=None,
                 shipping_duration=APIHelper.SKIP,
                 holiday_sorting=APIHelper.SKIP):
        """Constructor for the CheckoutRequest class"""

        # Initialize members of the class
        self.order_date = order_date 
        if shipping_duration is not APIHelper.SKIP:
            self.shipping_duration = shipping_duration 
        self.cut_off_times = cut_off_times 
        if holiday_sorting is not APIHelper.SKIP:
            self.holiday_sorting = holiday_sorting 
        self.options = options 
        self.locations = locations 
        self.days = days 
        self.addresses = addresses 

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
        order_date = dictionary.get("OrderDate") if dictionary.get("OrderDate") else None
        cut_off_times = None
        if dictionary.get('CutOffTimes') is not None:
            cut_off_times = [CheckoutCutOffTime.from_dictionary(x) for x in dictionary.get('CutOffTimes')]
        options = dictionary.get("Options") if dictionary.get("Options") else None
        locations = dictionary.get("Locations") if dictionary.get("Locations") else None
        days = dictionary.get("Days") if dictionary.get("Days") else None
        addresses = None
        if dictionary.get('Addresses') is not None:
            addresses = [CheckoutAddress.from_dictionary(x) for x in dictionary.get('Addresses')]
        shipping_duration = dictionary.get("ShippingDuration") if dictionary.get("ShippingDuration") else APIHelper.SKIP
        holiday_sorting = dictionary.get("HolidaySorting") if "HolidaySorting" in dictionary.keys() else APIHelper.SKIP
        # Return an object of this model
        return cls(order_date,
                   cut_off_times,
                   options,
                   locations,
                   days,
                   addresses,
                   shipping_duration,
                   holiday_sorting)
